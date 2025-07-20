```cpp
  
#define ot long long  
#define ld long double  
#define eps 1e-8    
#define vec(a, b) ((b)-(a))  
#define len(v) (hypotl((v).y, (v).x))  
  
struct P  
{  
    ot x, y;  
    void read()  
    {  
       cin >> x >> y;  
    }  
    P operator-(P const& he) const  
    {  
       return { x - he.x, y - he.y };  
    }  
    // cross product    
	ot operator^(P const& he) const  
    {  
       return x * he.y - y * he.x;  
    }  
};
```