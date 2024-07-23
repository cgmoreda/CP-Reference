
bool collinear(P a, P b, P c)  
{  
    return (vec(a, b) ^ vec(a, c)) == 0;  
}

inline ld angle(P a)  
{  
    return atan2((ld)a.y, (ld)a.x);  
}  


ld linePointDis(P l1, P l2, P p)  
{  
    ot area = abs(vec(p, l1) ^ vec(p, l2));  
    ld base = len(vec(l1, l2));  
    return area / base;  
}  
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
void sortAntiClockWise(vector<P>& pnts)  
{  
    P mn(*min_element(all(pnts)));  
    sort(pnts.begin(), pnts.end(), cmp(mn));  
}  
void convexHull(vector<P> p, vector<P>& hull)  
{  
  
    sort(all(p), [&](P& a, P& b)  
    {  
      if (a.x != b.x)  
         return a.x < b.x;  
      return a.y < b.y;  
    });  
    if (p.size() == 1)  
    {  
       hull.push_back(p[0]);  
       return;  
    }  
    for (int rep = 0; rep < 2; rep++)  
    {  
       int s = hull.size();  
       for (int i = 0; i < p.size(); i++)  
       {  
          while (hull.size() >= s + 2)  
          {  
             P p1 = hull.end()[-2];  
             P p2 = hull.end()[-1];  
             if ((vec(p1, p2) ^ vec(p1, p[i])) < -eps)  
                break;  
  
             hull.pop_back();  
          }  
          hull.push_back(p[i]);  
       }  
       reverse(all(p));  
       hull.pop_back();  
    }  
}  
P getCentroid(vector<P>& p)  
{  
    ld x, y;  
    long long tarea = 0;  
    x = 0;  
    y = 0;  
    for (int i = 1; i < p.size() - 2; i++)  
    {  
       long long area = (vec(p[0], p[i]) ^ vec(p[0], p[i + 1]));  
       x += area * ((p[0].x + p[i].x + p[i + 1].x) / 3.0);  
       y += area * ((p[0].y + p[i].y + p[i + 1].y) / 3.0);  
       tarea += area;  
    }  
    x /= tarea;  
    y /= tarea;  
    return P(x, y);  
}  
inline bool pibb(P const& a, P const& b1, P const& b2)  
{  
    return a.x >= min(b1.x, b2.x) &&  
       a.x <= max(b1.x, b2.x) &&  
       a.y >= min(b1.y, b2.y) &&  
       a.y <= max(b1.y, b2.y);  
}  
  
bool lineIntersection(P p1, P p2, P p3, P p4, P& sec)  
{  
    ld denom = (p1.x - p2.x) * (p3.y - p4.y) - (p1.y - p2.y) * (p3.x - p4.x);  
  
    if (abs(denom) < eps)  
       return false;  
  
    ld t = ((p1.x - p3.x) * (p3.y - p4.y) - (p1.y - p3.y) * (p3.x - p4.x)) / denom;  
  
    sec = p1 + vec(p1, p2) * t;  
  
    return true;  
}  
  
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
bool isPointOnSegment(P const& a, P const& l1, P const& l2)  
{  
    return collinear(a, l1, l2) && pibb(a, l1, l2);  
}  