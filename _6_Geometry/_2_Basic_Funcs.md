
```cpp
bool collinear(P a, P b, P c)  
{  
    return (vec(a, b) ^ vec(a, c)) == 0;  
}
```

**get acute directed angle from a to b**  
```cpp
ld gda(P a, P b)  
{  
    ld ang = abs(angle(a) - angle(b));  
    ang = min(ang, 2 * PI - ang);  
    return ang * ((a ^ b) > 0 ? 1 : -1);  
}
```

```cpp  
// get's X given a line and y
ld getX(P a, P b, ll y) {  
    ld slope = (b.y - a.y) / (b.x - a.x);  
    return a.x + (y - a.y) / slope;  
}
```

```cpp
ld linePointDis(P l1, P l2, P p)  
{  
    ot area = abs(vec(p, l1) ^ vec(p, l2));  
    ld base = len(vec(l1, l2));  
    return area / base;  
}  
```

```cpp
ld segmentPointDis(P l1, P l2, P p)  
{  
    P perp = vec(l1, l2);  
    perp.x *= -1;  
    perp = p + perp;  
    ld s1 = vec(p, perp) ^ vec(p, l1);  
    ld s2 = vec(p, perp) ^ vec(p, l2);  
    if ((s1 < 0 && s2 < 0) || (s1 > 0 && s2 > 0))  
       return min(len(vec(p, l1)), len(vec(p, l2)));  
    return linePointDis(l1, l2, p);  
}  
```

```cpp
struct cmp  
{  
    P about;  
    cmp(P c)  
    {  
       about = c;  
    }  
    bool operator()(const P& a, const P& b) const  
    {  
       ld cr = vec(about, a) ^ vec(about, b);  
       if (fabs(cr) < eps)  
          return a < b;  
       return cr > 0;  
    }  
};  
```

```cpp
void sortAntiClockWise(vector<P>& pnts)  
{  
    P mn(*min_element(all(pnts)));  
    sort(pnts.begin(), pnts.end(), cmp(mn));  
}  
inline bool pibb(P const& a, P const& b1, P const& b2)  
{  
    return a.x >= min(b1.x, b2.x) &&  
       a.x <= max(b1.x, b2.x) &&  
       a.y >= min(b1.y, b2.y) &&  
       a.y <= max(b1.y, b2.y);  
}  
```  

```cpp
bool lineIntersection(P p1, P p2, P p3, P p4, P& sec)  
{  
    ld denom = (p1.x - p2.x) * (p3.y - p4.y) - (p1.y - p2.y) * (p3.x -p4.x);  
  
    if (abs(denom) < eps)  
       return false;  
  
    ld t = ((p1.x - p3.x) * (p3.y - p4.y) - (p1.y - p3.y) * (p3.x - p4.x)) / denom;  
  
    sec = p1 + vec(p1, p2) * t;  
  
    return true;  
}  
```
  
```cpp
bool segmentsIntersection(P l1, P l2, P k1, P k2, P& sec)  
{  
    if (lineIntersection(l1, l2, k1, k2, sec))  
    {  
       if (pibb(sec, l1, l2) && pibb(sec, k1, k2))  
          return true;  
       return false;  
    }  
    return false;  
}  
```

```cpp
bool isPointOnSegment(P const& a, P const& l1, P const& l2)  
{  
    return collinear(a, l1, l2) && pibb(a, l1, l2);  
}  
```
```cpp
P getCircleCenter(P A, P B, P C) {  
    if (isCollinear(A, B, C)) {  
       collinear = true;  
       return {0, 0};   
    }  
    collinear = false;  
    ld D = 2 * (A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y));  
    ld Ux = ((A.x * A.x + A.y * A.y) * (B.y - C.y) + (B.x * B.x + B.y * B.y) * (C.y - A.y) + (C.x * C.x + C.y * C.y) * (A.y - B.y)) / D;  
    ld Uy = ((A.x * A.x + A.y * A.y) * (C.x - B.x) + (B.x * B.x + B.y * B.y) * (A.x - C.x) + (C.x * C.x + C.y * C.y) * (B.x - A.x)) / D;  
    return {Ux, Uy};  
}
```
  
```cpp
bool issqare(P a, P b, P c, P d)  
{  
    if (a == b || a == c || a == d || b == c || b == c || c == d)  
       return false;  
  
    vector<ld> ds = {  
       a.dis(b), a.dis(c), a.dis(d),  
       b.dis(c), b.dis(d), c.dis(d)  
    };  
    sort(all(ds));  
    return ds[0] > 0 &&  
       abs(ds[2] - ds[3]) < 1e-8 &&  
       abs(ds[0] - ds[1]) < 1e-8 &&  
       abs(ds[1] - ds[2]) < 1e-8 &&  
       abs(ds[4] - ds[5]) < 1e-8;  
  
}
```