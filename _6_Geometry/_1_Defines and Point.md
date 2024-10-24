#define ot long long  
#define ld long double  
#define sq(x) ((x)*(x))  
#define eps 1e-8  
#define angle(a) (atan2((a).y, (a).x))  
#define slope(p) (((p).y)/((p).x))  
#define vec(a, b) ((b)-(a))  
#define len(v) (hypot((v).y, (v).x))  
  
struct P  
{  
    ot x, y;  
    void read()  
    {  
       cin >> x >> y;  
    }  
  
    bool operator==(P const& he) const  
    {  
       return x == he.x && y == he.y;  
    }  
    P operator-(P const& he) const  
    {  
       return { x - he.x, y - he.y };  
    }  
  
    P operator+(P const& he) const  
    {  
       return { x + he.x, y + he.y };  
    }  
    void operator-=(P const& he)  
    {  
       x -= he.x, y -= he.y;  
    }  
    void operator+=(P const& he)  
    {  
       x += he.x, y += he.y;  
    }  
    // scalar multiplication  
    P operator*(ot val) const  
    {  
       return { x * val, y * val };  
    }  
  
    // cross product   
ot operator^(P const& he) const  
    {  
       return x * he.y - y * he.x;  
    }  
    // dot product = x1x2+y1y2 = |a|*|b|*cos(theta)  
    ot operator*(P const& he) const  
    {  
       return x * he.x + y * he.y;  
    }  
    ld dis(P he)  
    {  
       return sqrt(sq(he.x - x) + sq(he.y - y));  
    }  
  
    //angle in radians  
    P rotate(ot angle) const  
    {  
       ot cos_theta = cos(angle);  
       ot sin_theta = sin(angle);  
       return { x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta };  
    }  
};  