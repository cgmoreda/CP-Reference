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