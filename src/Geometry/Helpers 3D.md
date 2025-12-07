```cpp
#define vec3(a,b) ((b)-(a))

ld dis(P3 a, P3 b) { return vec3(a, b).len(); }

// scalar triple product: a · (b × c)
ld mixed(P3 a, P3 b, P3 c) { return a * (b ^ c); }
```

```cpp
bool collinear(P3 a, P3 b, P3 c){
    P3 ab = vec3(a,b), ac = vec3(a,c);
    return (ab ^ ac).len() <= eps * ab.len() * ac.len();
}
bool collinear(P3 a, P3 b, P3 c){
    P3 ab = vec3(a,b), ac = vec3(a,c);
    return (ab ^ ac).len() <= eps * ab.len() * ac.len();
}

bool coplanar(P3 a, P3 b, P3 c, P3 d){
    P3 ab=vec3(a,b), ac=vec3(a,c), ad=vec3(a,d);
    return fabsl(mixed(ab,ac,ad)) <= eps * ab.len() * ac.len() * ad.len();
}
bool coplanar(P3 a, P3 b, P3 c, P3 d){
    P3 ab=vec3(a,b), ac=vec3(a,c), ad=vec3(a,d);
    return fabsl(mixed(ab,ac,ad)) <= eps * ab.len() * ac.len() * ad.len();
}

```

```cpp
ld triArea(P3 a, P3 b, P3 c) {
    return (vec3(a, b) ^ vec3(a, c)).len() / 2;
}

ld tetraVol(P3 a, P3 b, P3 c, P3 d) {
    return fabsl(mixed(vec3(a, b), vec3(a, c), vec3(a, d))) / 6;
}
```
 
```cpp
// projection of p onto infinite line (a,b)
P3 projPointLine(P3 p, P3 a, P3 b) {
    P3 ab = vec3(a, b);
    ld ab2 = ab * ab;
    if (ab2 < eps) return a;
    ld t = (vec3(a, p) * ab) / ab2;
    return a + ab * t;
}
```

```cpp
ld linePointDis(P3 a, P3 b, P3 p) {
    P3 ab = vec3(a, b), ap = vec3(a, p);
    ld den = ab.len();
    if (den < eps) return ap.len();
    return (ab ^ ap).len() / den;
}

ld segmentPointDis(P3 a, P3 b, P3 p) {
    P3 ab = vec3(a, b), ap = vec3(a, p);
    ld ab2 = ab * ab;
    if (ab2 < eps) return ap.len();
    ld t = (ap * ab) / ab2;
    t = std::max<ld>(0, std::min<ld>(1, t));
    return dis(p, a + ab * t);
}

ld pointPlaneDis(P3 p, P3 A, P3 B, P3 C) {
    P3 n = (vec3(A, B) ^ vec3(A, C));
    ld den = n.len();
    if (den < eps) return 0;
    return fabsl(vec3(A, p) * n) / den;
}

```
 
```cpp
// projection of p onto plane (A,B,C)
P3 projPointPlane(P3 p, P3 A, P3 B, P3 C) {
    P3 n = (vec3(A, B) ^ vec3(A, C));
    ld nn = n * n;
    if (nn < eps) return p;
    ld t = (vec3(A, p) * n) / nn;
    return p - n * t;
}

// reflection of p across plane (A,B,C)
P3 reflectPointPlane(P3 p, P3 A, P3 B, P3 C) {
    P3 q = projPointPlane(p, A, B, C);
    return q * 2 - p;
}

```

```cpp
ld angle3(P3 a, P3 b) { // [0, pi]
    ld la = a.len(), lb = b.len();
    if (la < eps || lb < eps) return 0;
    ld cs = (a * b) / (la * lb);
    cs = std::max<ld>(-1, std::min<ld>(1, cs));
    return acosl(cs);
}
```

```cpp
// line (p1,p2) with plane (A,B,C) -> unique intersection point in 'sec'
bool linePlaneIntersection(P3 p1, P3 p2, P3 A, P3 B, P3 C, P3& sec) {
    P3 v = vec3(p1, p2);
    P3 n = (vec3(A, B) ^ vec3(A, C));
    ld denom = n * v;
    if (fabsl(denom) < eps) return false; // parallel or in-plane -> no unique hit
    ld t = (n * (A - p1)) / denom;
    sec = p1 + v * t;
    return true;
}

// segment [p1,p2] with plane (A,B,C) -> unique intersection in 'sec'
bool segmentPlaneIntersection(P3 p1, P3 p2, P3 A, P3 B, P3 C, P3& sec) {
    P3 v = vec3(p1, p2);
    P3 n = (vec3(A, B) ^ vec3(A, C));
    ld denom = n * v;
    if (fabsl(denom) < eps) return false;
    ld t = (n * (A - p1)) / denom;
    if (t < -eps || t > 1 + eps) return false;
    sec = p1 + v * t;
    return true;
}
```

```cpp
// point-in-triangle in 3D (accepts points slightly off-plane within eps)
bool pointInTriangle(P3 p, P3 A, P3 B, P3 C) {
    P3 n = (vec3(A, B) ^ vec3(A, C));
    ld nl = n.len();
    if (nl < eps) return false; // degenerate triangle
    if (fabsl(vec3(A, p) * n) > eps * nl) return false; // not on plane

    P3 v0 = vec3(A, C), v1 = vec3(A, B), v2 = vec3(A, p);
    ld d00 = v0 * v0, d01 = v0 * v1, d11 = v1 * v1;
    ld d20 = v2 * v0, d21 = v2 * v1;
    ld denom = d00 * d11 - d01 * d01;
    if (fabsl(denom) < eps) return false;

    ld u = (d11 * d20 - d01 * d21) / denom;
    ld v = (d00 * d21 - d01 * d20) / denom;
    return u >= -eps && v >= -eps && u + v <= 1 + eps;
}
```