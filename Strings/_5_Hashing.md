```cpp
const int N = 1e5 + 5, MOD1 = 1e9 + 7, MOD2 = 1e9 + 9;
	int pw1[N], inv1[N], pw2[N], inv2[N], BASE;

bool isPrime(int x) {
    for (int i = 2; i * i <= x; i++) {
        if (x % i == 0) return 0;
    }
    return x > 1;
}

int fix(ll x, int M) {
    return (x % M + M) % M;
}

int fpow(int a, int b, int mod) {
    if (!b) return 1;
    int ret = fpow(a, b >> 1, mod);
    ret = fix(1ll * ret * ret, mod);
    if (b & 1) ret = fix(1ll * ret * a, mod);
    return ret;
}

void init() {
    static bool done = false;
    if (done) return;
    done = true;
    
    mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
    uniform_int_distribution<int> dist(257, 10007);
    do{
        BASE = dist(rng);
    }while (!isPrime(BASE));

    pw1[0] = inv1[0] = pw2[0] = inv2[0] = 1;
    int iv1 = fpow(BASE, MOD1 - 2, MOD1);
    int iv2 = fpow(BASE, MOD2 - 2, MOD2);
    for (int i = 1; i < N; ++i) {
        pw1[i] = fix(1ll * pw1[i - 1] * BASE, MOD1);
        pw2[i] = fix(1ll * pw2[i - 1] * BASE, MOD2);
        inv1[i] = fix(1ll * inv1[i - 1] * iv1, MOD1);
        inv2[i] = fix(1ll * inv2[i - 1] * iv2, MOD2);
    }
}

struct Hash {
    vector<pair<int, int>> pre;

    Hash(const string &s) {
        init();
        pre.assign(sz(s) + 1, {0, 0});
        for (int i = 0; i < sz(s); i++) {
            pre[i + 1] = make_pair(fix(1ll * pw1[i] * s[i] + pre[i].first, MOD1),
                                   fix(1ll * pw2[i] * s[i] + pre[i].second, MOD2));
        }
    }

    pair<int, int> getRange(int l, int r) const { // 0-based
        return make_pair(fix(1ll * inv1[l] * (pre[r + 1].first - pre[l].first), MOD1),
                         fix(1ll * inv2[l] * (pre[r + 1].second - pre[l].second), MOD2));
    }
};
```