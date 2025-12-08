```cpp
const ll mod = (119 << 23) + 1, root = 3; // = 998244353
// For p < 2^30 there is also e.g. 5 << 25, 7 << 26, 479 << 21
// and 483 << 21 (same root). The last two are > 10^9.
ll modpow(ll b, ll e) {
    ll ans = 1;
    for (; e; b = b * b % mod, e /= 2)
        if (e & 1) ans = ans * b % mod;
    return ans;
}

// Primitive Root of the mod of form 2^a * b + 1
int generator() {
    vector<int> fact;
    int phi = mod - 1, n = phi;
    for (int i = 2; i * i <= n; ++i)
        if (n % i == 0) {
            fact.push_back(i);
            while (n % i == 0)
                n /= i;
        }
    if (n > 1)
        fact.push_back(n);

    for (int res = 2; res <= mod; ++res) {
        bool ok = true;
        for (size_t i = 0; i < fact.size() && ok; ++i)
            ok &= modpow(res, phi / fact[i]) != 1;
        if (ok) return res;
    }
    return -1;
}

ll modpow(ll b, ll e, ll m) {
    ll ans = 1;
    for (; e; b = b * b % m, e /= 2)
        if (e & 1) ans = ans * b % m;
    return ans;
}

void ntt(vector<ll> &a) {
    int n = (int) a.size(), L = 31 - __builtin_clz(n);
    static vector<ll> rt(2, 1); // erase the static if you want to use two moduli;
    for (static int k = 2, s = 2; k < n; k *= 2, s++) { // erase the static if you want to use two moduli;
        rt.resize(n);
        ll z[] = {1, modpow(root, mod >> s, mod)};
        for (int i = k; i < 2 * k; ++i) rt[i] = rt[i / 2] * z[i & 1] % mod;
    }
    vector<int> rev(n);
    for (int i = 0; i < n; ++i) rev[i] = (rev[i / 2] | (i & 1) << L) / 2;
    for (int i = 0; i < n; ++i) if (i < rev[i]) swap(a[i], a[rev[i]]);
    for (int k = 1; k < n; k *= 2) {
        for (int i = 0; i < n; i += 2 * k) {
            for (int j = 0; j < k; ++j) {
                ll z = rt[j + k] * a[i + j + k] % mod, &ai = a[i + j];
                a[i + j + k] = ai - z + (z > ai ? mod : 0);
                ai += (ai + z >= mod ? z - mod : z);
            }
        }
    }
}

vector<ll> conv(const vector<ll> &a, const vector<ll> &b) {
    if (a.empty() || b.empty()) return {};
    int s = (int) a.size() + (int) b.size() - 1, B = 32 - __builtin_clz(s), n = 1 << B;
    int inv = modpow(n, mod - 2, mod);
    vector<ll> L(a), R(b), out(n);
    L.resize(n), R.resize(n);
    ntt(L), ntt(R);
    for (int i = 0; i < n; ++i) out[-i & (n - 1)] = (ll) L[i] * R[i] % mod * inv % mod;
    ntt(out);
    return {out.begin(), out.begin() + s};
}

vector<ll> polyPow(vector<ll> a, ll k) {
    vector<ll> ans = {1};
    while (k) {
        if (k & 1) {
            ans = conv(ans, a);
        }
        k >>= 1;
        a = conv(a, a);
    }
    return ans;
}

const int N = 1e6 + 100;
ll fact[N];
ll inv[N]; //mod inverse for i
ll invfact[N]; //mod inverse for i!
//call factInverse
void factInverse() {
    fact[0] = inv[1] = fact[1] = invfact[0] = invfact[1] = 1;
    for (long long i = 2; i < N; i++) {
        fact[i] = (fact[i - 1] * i) % mod;
        inv[i] = mod - (inv[mod % i] * (mod / i) % mod);
        invfact[i] = (inv[i] * invfact[i - 1]) % mod;
    }
}
//t(x) -> t(x + k) or t(x - k)
vector<ll> shift(const vector<ll> &p, ll k) {
    k %= mod;
    k += mod;
    k %= mod;

    ll n = p.size();
    vector<ll> p1(n), p2(n);
    for (int i = 0; i < n; ++i) {
        p1[i] = fact[i] * p[i] % mod;
    }

    ll curr = 1;
    for (int i = 0; i < n; ++i) {
        p2[n - i - 1] = invfact[i] * curr % mod;
        curr = curr * k % mod;
    }

    vector<ll> res = conv(p1, p2);

    vector<ll> ans;
    for (int i = n - 1; i < res.size(); ++i) {
        ans.push_back(res[i] * invfact[i - (n - 1)] % mod);
    }

    return ans;
}
```