

ld areaOfTri(P a, P b, P c)  
{  
    return abs((vec(a, b) ^ vec(a, c)) / 2.0);  
}  

ld triArea(ot A, ot B, ot C)  
{  
    ld s = (A + B + C) * 0.5;  
    return sqrt(s * (s - A) * (s - B) * (s - C));  
}

ld areaOfPolygon(vector<P> p)  
{  
    ot area = 0;  
    for (int i = 1; i < p.size() - 1; i++)  
       area += vec(p[0], p[i]) ^ vec(p[0], p[i + 1]);  
  
    return abs(area / 2.0);  
}  