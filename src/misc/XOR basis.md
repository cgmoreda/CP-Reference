```cpp
const int d=31;
int basis[d];
int sz;
bool insertVector(int mask) {
    for (ll i = d-1;i>=0; i--){
        if ((mask & 1<< i) == 0) continue;
        if (!basis[i]) {
            basis[i] = mask;
            sz++;
            return true;
        }
        mask ^= basis[i];
    }
    return false;
}
```
Xor Basis Extended version
```cpp
struct xorBasis
{
    const int LG = 62;
    vector<ll> basis;
    int sz;

    xorBasis()
    {
        sz = 0;
        basis = vector<ll>(LG);
    }

    bool insert(ll mask)
    {
        for (int i = LG - 1; i >= 0; i--)
        {
            if ((mask >> i) & 1)
            {
                if (!basis[i])
                {
                    basis[i] = mask;
                    sz++;
                    return true;
                }
                mask ^= basis[i];
            }
        }
        return false;
    }

    bool find(ll mask)
    {
        for (int i = LG - 1; i >= 0; i--)
        {
            if ((mask >> i) & 1)
            {
                if (!basis[i])
                {
                    return false;
                }
                mask ^= basis[i];
            }
        }
        return true;
    }

    ll mx_xor()
    {
        ll ans = 0;
        for (int i = LG - 1; i >= 0; i--)
        {
            ans = max(ans, ans ^ basis[i]);
        }
        return ans;
    }

    // k base 0
    ll kth_distinct_xor(ll k)
    {
        if (k >= (1ll << sz)) return -1;
        ll ans = 0, c = 1ll << sz;
        for (int i = LG - 1; i >= 0; i--)
        {
            if (!basis[i])continue;
            c >>= 1;
            int on = ans >> i & 1;
            if ((k < c) == on)ans ^= basis[i];
            if (k >= c)k -= c;
        }
        return ans;
    }

    ll kth_xor(ll k, const ll& n)
    {
        ll dup = n - sz;
        if (dup >= 62)
        {
            k = 0;
        }
        else
        {
            k >>= dup;
        }
        return kth_distinct_xor(k);
    }

    // Count how many distinct subset XORs < x
    ll count_lt(ll x)
    {
        ll ans = 0, cnt = 1LL << sz, mask = 0;
        for (int i = LG - 1; i >= 0; --i)
        {
            if (basis[i])
            {
                if ((x >> i) & 1)
                {
                    ans += (cnt >> 1);
                    if (!((mask >> i) & 1))
                        mask ^= basis[i];
                }
                else
                {
                    if ((mask >> i) & 1)
                        mask ^= basis[i];
                }
                cnt >>= 1;
            }
            else
            {
                if (((x >> i) & 1) != ((mask >> i) & 1))
                {
                    return ((x >> i) & 1) ? ans + cnt : ans;
                }
            }
        }
        return ans;
    }
};
```
