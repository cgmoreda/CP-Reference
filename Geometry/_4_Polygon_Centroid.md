```cpp  
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
    return { x, y };  
}
```