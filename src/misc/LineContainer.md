```cpp
struct Line {
    ll m, c;
    mutable ll p; //p is intersection between cur and next
    bool operator<(const Line &o) const {
        //change to (m>o.m,c < o.c) to get min
        if (m != o.m)
            return m < o.m;
        return c > o.c;
    }
    bool operator<(ll x) const {
        return p < x;
    }
};

struct LineContainer: multiset<Line, less<>> {
    // (for doubles, use inf = INFINITY, div(a,b) = a/b)
    static const ll inf = LLONG_MAX;
    ll div(ll a, ll b) { // floored division
        return a / b - ((a ^ b) < 0 && a % b);
    }
    bool isect(iterator x, iterator y) {
        if (y == end())
            return x->p = inf, 0;
        if (x->m == y->m)
            x->p = inf;
        else
            x->p = div(y->c - x->c, x->m - y->m);
        return x->p >= y->p;
    }
    void add(ll m, ll c) {
        auto z = insert( { m, c, 0 }), y = z++, x = y;
        while (isect(y, z))
            z = erase(z);
        if (x != begin() && isect(--x, y))
            isect(x, y = erase(y));
        while ((y = x) != begin() && (--x)->p >= y->p)
            isect(x, erase(y));
    }
    ll query(ll x) {
        assert(!empty());
        auto l = *lower_bound(x);
        return l.m * x + l.c;
    }
};
```