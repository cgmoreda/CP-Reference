```cpp
ll mxb(ll x)  
{  
   if (!x)  
      return x;  
   return 1LL << (63 - __builtin_clzll(x));  
}
// count leading zeros
__builtin_clzll(x)

// count on bits 
__builtin_popcountll(x)

// to get lowbit (x&-x)

```