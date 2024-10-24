//xor from 1 to x  
ll getXor(ll x) {  
    if (x % 4 == 0)return x;  
    if (x % 4 == 1)return 1;  
    if (x % 4 == 2)return x + 1;  
    return 0;  
}