// return a ^ 1 + a ^ 2 + a ^ 3 + .... a ^ k  
ll sumPower(ll a, ll k, int mod) {  
    if (k == 1) return a % mod;  
    ll half = sumPower(a, k / 2, mod);  
    ll p = half * power(a, k / 2, mod) % mod;  
    p = (p + half) % mod;  
    if (k & 1) p = (p + power(a, k, mod)) % mod;  
    return p;  
}
// same function but faster 
int calci_xpi(int x, int n)  
{  
    int p1 = fix(fix(x * (1 - (modInv(Bpow(x, n))))) * modInv((x - 1) * (x - 1)));  
    int p2 = fix(n * fix(modInv((x - 1) * Bpow(x, n))));  
    return fix(p1 - p2);  
}

//return sum of sequence a, a+x , a+2x .... b  
ll sumSequence(ll a, ll b, ll x) {  
    a = ((a + x - 1) / x) * x;  
    b = (b / x) * x;  
    return (b + a) * (b - a + x) / (2 * x);  
}
