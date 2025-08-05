```cpp
// n < 4,759,123,141        3 :  2, 7, 61  
// n < 1,122,004,669,633    4 :  2, 13, 23, 1662803  
// n < 3,474,749,660,383          6 :  pirmes <= 13  
// n < 2^64                       7 :  
// 2, 325, 9375, 28178, 450775, 9780504, 1795265022  
// Make sure testing integer is in range [2, n−2] if
//The largest known gap between consecutive primes ≤ 1e9 is 282, ≤ 1e12 ≤ 1132
using u64 = uint64_t;
using u128 = __uint128_t;
u64 binpower(u64 base, u64 e, u64 mod) {
    u64 result = 1;
    base %= mod;
    while (e) {
        if (e & 1)
            result = (u128) result * base % mod;
        base = (u128) base * base % mod;
        e >>= 1;
    }
    return result;
}
bool check_composite(u64 n, u64 a, u64 d, int s) {
    u64 x = binpower(a, d, n);
    if (x == 1 || x == n - 1)
        return false;
    for (int r = 1; r < s; r++) {
        x = (u128) x * x % n;
        if (x == n - 1)
            return false;
    }
    return true;
}
bool MillerRabin(u64 n) { // returns true if n is prime, else returns false.
    if (n < 2)
        return false;

    int r = 0;
    u64 d = n - 1;
    while ((d & 1) == 0) {
        d >>= 1;
        r++;
    }

    for (int a: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
        if (n == a)
            return true;
        if (check_composite(n, a, d, r))
            return false;
    }
    return true;
}
```