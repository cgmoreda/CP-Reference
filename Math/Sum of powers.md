// return a ^ 1 + a ^ 2 + a ^ 3 + .... a ^ k  
ll sumPower(ll a, ll k, int mod) {  
    if (k == 1) return a % mod;  
    ll half = sumPower(a, k / 2, mod);  
    ll p = half * power(a, k / 2, mod) % mod;  
    p = (p + half) % mod;  
    if (k & 1) p = (p + power(a, k, mod)) % mod;  
    return p;  
}