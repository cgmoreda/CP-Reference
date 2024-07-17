
int calci_xpi(int x, int n)  
{  
    int p1 = fix(fix(x * (1 - (modInv(Bpow(x, n))))) * modInv((x - 1) * (x - 1)));  
    int p2 = fix(n * fix(modInv((x - 1) * Bpow(x, n))));  
    return fix(p1 - p2);  
}