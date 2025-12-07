```cpp
const int LC_N = (int)1e6 + 1;
const long long LC_INF = (long long)1e17;
vector<array<long long,2>> lc_tree(4 * LC_N, {0, LC_INF});

long long f_line(const array<long long,2>& line, int x) {
    return line[0] * x + line[1];
}

void lc_insert(array<long long,2> line, int lo = 1, int hi = LC_N, int i = 1) {
    int m = (lo + hi) / 2;
    bool left = f_line(line, lo) < f_line(lc_tree[i], lo);
    bool mid  = f_line(line, m)  < f_line(lc_tree[i], m);

    if (mid) swap(lc_tree[i], line);
    if (hi - lo == 1) return;

    if (left != mid)
        lc_insert(line, lo, m, 2 * i);
    else
        lc_insert(line, m, hi, 2 * i + 1);
}

long long lc_query(int x, int lo = 1, int hi = LC_N, int i = 1) {
    int m = (lo + hi) / 2;
    long long curr = f_line(lc_tree[i], x);

    if (hi - lo == 1) return curr;

    if (x < m)
        return min(curr, lc_query(x, lo, m, 2 * i));
    else
        return min(curr, lc_query(x, m, hi, 2 * i + 1));
}
```