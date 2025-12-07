```cpp
ld areaOfTri(P a, P b, P c){  
    return abs((vec(a, b)^vec(a, c)) / 2.0);  
}  
```

```cpp
ld triArea(ot A, ot B, ot C){  
    ld s = (A + B + C) * 0.5;  
    return sqrt(s * (s - A) * (s - B) * (s - C));  
} 
``` 
//Area of a Triangle Formula in Coordinate Geometry  
//If (x1, y1), (x2, y2), and (x3, y3) are the three vertices of a triangle on the coordinate plane, then //its area is calculated by the formula  
//(1/2) |x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)|  

```cpp 
// tested
ld areaOfPolygon(vector<P> p){  
    ot area = 0;  
    for(int i = 1; i < p.size() - 1; i++)  
       area += vec(p[0], p[i])^vec(p[0], p[i + 1]);  
    return abs(area / 2.0);  
}
```