```cpp
// 3D geometry (compact, ACPC-friendly)

#define ot long long
#define ld long double
#define sq(x) ((x)*(x))

const ld eps = 1e-12L;
const ld PI  = acosl(-1.0L);

struct P3 {
    ld x, y, z;

    void read() { std::cin >> x >> y >> z; }

    P3 operator + (P3 const& o) const { return {x + o.x, y + o.y, z + o.z}; }
    P3 operator - (P3 const& o) const { return {x - o.x, y - o.y, z - o.z}; }
    void operator += (P3 const& o) { x += o.x; y += o.y; z += o.z; }
    void operator -= (P3 const& o) { x -= o.x; y -= o.y; z -= o.z; }

    P3 operator * (ld k) const { return {x * k, y * k, z * k}; }
    P3 operator / (ld k) const { return {x / k, y / k, z / k}; }
    friend P3 operator * (ld k, P3 a) { return a * k; }

    // dot
    ld operator * (P3 const& o) const { return x * o.x + y * o.y + z * o.z; }

    // cross
    P3 operator ^ (P3 const& o) const {
        return { y * o.z - z * o.y, z * o.x - x * o.z, x * o.y - y * o.x };
    }

    ld norm2() const { return (*this) * (*this); }
    ld len()   const { return sqrtl(norm2()); }

    P3 unit() const {
        ld l = len();
        return (l < eps ? P3{0, 0, 0} : (*this) / l);
    }

    // Rodrigues rotation: rotate this vector around 'axis' (through origin) by 'ang' radians
    P3 rotate(P3 axis, ld ang) const {
        axis = axis.unit();
        if (axis.len() < eps) return *this;
        ld c = cosl(ang), s = sinl(ang);
        return (*this) * c + (axis ^ (*this)) * s + axis * ((axis * (*this)) * (1 - c));
    }
};
```