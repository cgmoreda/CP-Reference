// return sum of divisors for all number from 1 to n //O(n)  
```cpp
ll sumRangeDivisors(int n) {  
    ll ans = 0;  
      
    for (int x = 1; x <= n; x++)  
        ans += (n / x) * x;  
    return ans;  
}  
```
// calc 1e9 in 42ms,can calc more but need big integer  
```cpp
ll sumRangeDivisors(ll x) {  
    ll ans = 0, left = 1, right;  
    for (; left <= x; left = right + 1) {  
        right = x / (x / left);  
        ans += (x / left) * (left + right) * (right - left + 1) / 2;  
    }  
    return ans;  
}
```