```cpp
// (a^n)%p=result, return minimum n
int getPower(int a, int result, int mod) {
    int sq = sqrt(mod);
    map<int, int> mp;
    ll r = 1;
    for (int i = 0; i < sq; i++) {
        if (mp.find(r) == mp.end())
            mp[r] = i;
        r = (r * a) % mod;
    }
    ll tmp = modInverse(r, mod);
    ll cur = result;
    for (int i = 0; i <= mod; i += sq) {
        if (mp.find(cur) != mp.end())
            return i + mp[cur];
        cur = (cur * tmp) % mod;//val/(a^sq)
    }
    return INF;
}
```