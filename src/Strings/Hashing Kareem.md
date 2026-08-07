```cpp
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
```

```cpp
//prefix-suffix-hashing
class Hashing{
private:
    const ll mod = (1ll << 61) - 1;
    static ll base;
    int sz;
    vector<ll>hPre,hSuf,pow;
    //pow[i] = base^i
public:
    Hashing(const string&s,char st = 'a'){ // 1-based
        sz = sz(s);
        hPre  = pow = hSuf = vector<ll>(sz + 1);
        pow[0] = 1;
        for(int i = 1; i <= sz;i++){
            pow[i] = (__int128_t)pow[i-1]*base % mod;
            hPre[i] = ((__int128_t)(s[i-1] - st + 1)*pow[i-1]  + hPre[i-1] )%mod;
        }
        for(int i = sz;i>0;i--){
            hSuf[i] = ((__int128_t)(s[i-1] - st  + 1)*(pow[sz - i])+ (i!= sz ? hSuf[i+1] : 0ll))%mod;
        }
    }
    ll prefix(int l,int r){ // l,r is 0-based biased to base^n
        return ((__int128_t)(hPre[r+1] - hPre[l])*pow[sz - r - 1]%mod + mod)%mod;
    }
    ll suffix(int l,int r){// l,r is 0-based biased to base^n
        return ((__int128_t)(hSuf[l+1] - (r+2 <= sz ? hSuf[r+2] : 0ll))*pow[l]%mod + mod)%mod;
    }
    bool isPalindrome(int l,int r){
        return prefix(l,r) == suffix(l,r);
    }
};
ll rng(ll l = (1ll << 40), ll r = (1ll << 60)) {
    static std::mt19937 gen(
            std::chrono::steady_clock::now().time_since_epoch().count());
    return std::uniform_int_distribution<long long>(l, r)(gen);
}
ll Hashing::base = rng();
```