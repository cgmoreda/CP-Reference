class Hashing {
    const ll MOD = (1ll << 61) - 1;
    vector<ll> p, h;
    static ll base;
public:
    Hashing(const string &a) {
        p = h = vector<ll>(a.size() + 1);
        p[0] = 1;
        for (int i = 0; i < a.size(); i++) {
            p[i+1] = (__int128_t) p[i] * base % MOD;
            h[i+1] = ((__int128_t) h[i] * base + a[i]) % MOD;
        }
    }
    ll getHash(int l, int r) { //base 0
        return ((h[r + 1] - (__int128_t) h[l] * p[r - l + 1] % MOD) + MOD)%MOD;
    }
};
ll rng(ll l = (1ll << 40), ll r = (1ll << 60)) {
    static std::mt19937 gen(
            std::chrono::steady_clock::now().time_since_epoch().count());
    return std::uniform_int_distribution<long long>(l, r)(gen);
}
ll Hashing::base = rng();