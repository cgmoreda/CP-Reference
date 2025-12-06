```cpp
ll fpow(ll x, ll n, int mod) {  
    if (n == 0)return 1 % mod;  
    if (n == 1)return x % mod;  
    ll ans = fpow(x, n / 2, mod);  
    ans = ans * ans % mod;  
    if (n & 1)ans = ans * (x % mod) % mod;  
    return ans;  
}
```


```cpp
 // iterative
ll fpow(ll x, ll k, ll mod) {
	ll res = 1;
	for (x %= mod; k; k >>= 1, x = x * x % mod)
		if (k & 1) res = res * x % mod;
	return res;
}
```

```cpp
// minimal 
ll fast(ll b, ll e){  
    if(!e)return 1;  
    return fast(b * b % mod, e >> 1) * ((e&1) ? b : 1) % mod;  
}
```

```cpp
ll modInverse(ll b, ll mod) { // if mod is Prime  
    return power(b, mod - 2, mod);  
}  
```
**if mod is not Prime,gcd(a,b) must be equal 1  
```cpp
ll modInverse(ll b, ll mod) { 
    return power(b, phi_function(mod) - 1, mod);  
}
```