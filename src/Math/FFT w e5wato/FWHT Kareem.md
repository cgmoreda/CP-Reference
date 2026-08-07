```cpp
//const int mod = 998244353;
// big mod if overflow can happen
const ll mod = 1000000000000000003LL;

// if using big mode add this
inline ll add(ll a, ll b) { return a + b >= mod ? a + b - mod : a + b; }

inline ll sub(ll a, ll b) { return a - b < 0 ? a - b + mod : a - b; }

inline ll mul_mod(ll a, ll b) { return 1LL * (__int128_t) a * b % mod; }

ll poww(ll a, ll b) {
    ll ret = 1;
    while (b) {
        if (b & 1) ret = mul_mod(ret,a);
        a = mul_mod(a, a);
        b >>= 1;
    }
    return ret;
}

void fwht(vector<ll> &a, int inv, int f) {
    ll sz = a.size();
    for (int len = 1; 2 * len <= sz; len <<= 1) {
        for (int i = 0; i < sz; i += 2 * len) {
            for (int j = 0; j < len; j++) {
                ll x = a[i + j];
                ll y = a[i + j + len];

                if (f == 0) { // AND
                    if (!inv) a[i + j] = add(x, y);
                    else a[i + j] = sub(x, y);
                } else if (f == 1) { // OR
                    if (!inv) a[i + j + len] = add(x, y);
                    else a[i + j + len] = sub(y, x);
                } else { // XOR
                    a[i + j] = add(x, y);
                    a[i + j + len] = sub(x, y);
                }
            }
        }
    }
}

vector<ll> mul(vector<ll> a, vector<ll> b, int f) { // 0:AND, 1:OR, 2:XOR
    ll mx = max(a.size(), b.size());
    ll sz = 1;
    while (sz < mx) sz <<= 1;
    a.resize(sz, 0);
    b.resize(sz, 0);
    fwht(a, 0, f);
    fwht(b, 0, f);
    vector<ll> c(sz);
    for (int i = 0; i < sz; ++i) {
        c[i] = mul_mod(a[i],b[i]);
        //can use raise to power trick instead of mul x times like normal FFT
        //c[i] = poww(c[i],x);
    }
    fwht(c, 1, f);
    if (f == 2) {
        ll sz_inv = poww(sz, mod - 2);
        for (int i = 0; i < sz; ++i) {
            //over flow use this
            c[i] = mul_mod(c[i],sz_inv);
        }
    }
    return c;
}
```