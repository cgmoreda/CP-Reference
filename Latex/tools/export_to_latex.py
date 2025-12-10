#!/usr/bin/env python3
import argparse
from pathlib import Path
import re

SKIP_DIRS = {".git", ".obsidian", "__pycache__", "Latex"}
SKIP_FILES = {".DS_Store"}
HEADINGS = ["section", "subsection", "subsubsection", "paragraph", "subparagraph"]

def latex_escape(text: str) -> str:
    repl = {
        "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
        "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}", "\\": r"\textbackslash{}",
    }
    for k, v in repl.items():
        text = text.replace(k, v)
    return text

def heading(text: str, depth: int, *, numbered: bool = True) -> str:
    cmd = HEADINGS[min(depth, len(HEADINGS) - 1)]
    safe = latex_escape(text)
    if numbered:
        return f"\\{cmd}{{{safe}}}"
    # unnumbered but still in TOC
    return "\n".join([
        f"\\{cmd}*{{{safe}}}",
        f"\\addcontentsline{{toc}}{{{cmd}}}{{{safe}}}"
    ])

def detect_language(body: str, default_lang: str) -> str:
    for match in re.finditer(r"^```([\w+-]+)?", body, flags=re.M):
        lang = (match.group(1) or "").strip()
        if lang:
            return lang
    return default_lang

def strip_fences(body: str) -> str:
    cleaned, in_fence = [], False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        cleaned.append(line.rstrip())
    # Expand tabs to spaces to avoid ^^I artifacts in LaTeX
    return "\n".join(cleaned).expandtabs(2).strip()

def render_file(path: Path, depth: int, default_lang: str, root: Path | None = None) -> str:
    raw = path.read_text(encoding="utf-8")
    lang = detect_language(raw, default_lang)
    content = strip_fences(raw)
    return "\n".join([
        heading(path.stem, depth),
        f"\\begin{{minted}}[fontsize=\\small, breaklines=true, breakanywhere=true, tabsize=2, obeytabs]{{{lang}}}",
        content,
        r"\end{minted}",
        "",
    ])

def process_dir(path: Path, depth: int, default_lang: str, root: Path) -> list[str]:
    parts = []
    files = sorted(
        [p for p in path.iterdir() if p.is_file() and p.suffix.lower() == ".md" and p.name not in SKIP_FILES],
        key=lambda p: p.name.lower(),
    )
    dirs = sorted(
        [p for p in path.iterdir() if p.is_dir() and p.name not in SKIP_DIRS],
        key=lambda p: p.name.lower(),
    )

    for f in files:
        parts.append(render_file(f, depth + 1, default_lang, root))

    for d in dirs:
        parts.append(heading(d.name, depth + 1, numbered=True))
        parts.extend(process_dir(d, depth + 1, default_lang, root))
    return parts

def main() -> None:
    parser = argparse.ArgumentParser(description="Export markdown notes to a LaTeX document with minted.")
    parser.add_argument("--root", default="src", type=Path, help="Vault root to export (default: src).")
    parser.add_argument("--output", "-o", default="CP_reference__3al_Hady_ACPC_2025_/main.tex", type=Path, help="Output LaTeX file.")
    parser.add_argument("--title", default="CP-Reference", help="Top-level document title.")
    parser.add_argument("--default-lang", default="cpp", help="Fallback language for minted.")
    args = parser.parse_args()

    root = args.root.resolve()
    parts = [
        r"\documentclass[14pt]{extarticle}",
        r"\usepackage{minted}",
        r"\usepackage[margin=0.8in]{geometry}",
        r"\usepackage{hyperref}",
        r"\usepackage{titlesec}",
        r"\usepackage{enumitem}",
        r"\linespread{0.9}",
        r"\titlespacing*{\section}{0pt}{1ex plus .5ex minus .2ex}{0.5ex}",
        r"\titlespacing*{\subsection}{0pt}{0.8ex plus .4ex minus .2ex}{0.4ex}",
        r"\titlespacing*{\subsubsection}{0pt}{0.6ex plus .3ex minus .2ex}{0.3ex}",
        r"\setlist{nosep,leftmargin=*}",
        r"\setminted{fontsize=\small, breaklines=true, breakanywhere=true, tabsize=2, obeytabs}",
        r"\setcounter{tocdepth}{3}",
        r"\setcounter{secnumdepth}{3}",
        "",
        r"\begin{document}",
        rf"\section*{{{latex_escape(args.title)}}}",
        r"\tableofcontents",
        "",
    ]
    # include only Template.md at the root; everything else must live in folders
    template_path = root / "Template.md"
    if template_path.exists():
        parts.append(render_file(template_path, 0, args.default_lang, root))

    top_dirs = sorted([p for p in root.iterdir() if p.is_dir() and p.name not in SKIP_DIRS], key=lambda p: p.name.lower())
    for d in top_dirs:
        parts.append(heading(d.name, 0, numbered=True))
        parts.extend(process_dir(d, 0, args.default_lang, root))

    parts.append(r"\end{document}")

    args.output.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {args.output}")

if __name__ == "__main__":
    main()
