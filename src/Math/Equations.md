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
// need testing
// return a ^ 1 + a ^ 2 + a ^ 3 + .... a ^ k  
```cpp
ll sumPower(ll a, ll k, int mod) {  
    if (k == 1) return a % mod;  
    ll half = sumPower(a, k / 2, mod);  
    ll p = half * power(a, k / 2, mod) % mod;  
    p = (p + half) % mod;  
    if (k & 1) p = (p + power(a, k, mod)) % mod;  
    return p;  
}
```
// same function but faster (not tested) 
```cpp
int calci_xpi(int x, int n)  
{  
    int p1 = fix(fix(x * (1 - (modInv(Bpow(x, n))))) * modInv((x - 1) * (x - 1)));  
    int p2 = fix(n * fix(modInv((x - 1) * Bpow(x, n))));  
    return fix(p1 - p2);  
}
```
//return sum of sequence a, a+x , a+2x .... b(not tested)  
```cpp
ll sumSequence(ll a, ll b, ll x) {  
    a = ((a + x - 1) / x) * x;  
    b = (b / x) * x;  
    return (b + a) * (b - a + x) / (2 * x);  
}
```