ll modInverse(ll b, ll mod) { // if mod is Prime  
    return power(b, mod - 2, mod);  
}  
  
ll modInverse(ll b, ll mod) { // if mod is not Prime,gcd(a,b) must be equal 1  
    return power(b, phi_function(mod) - 1, mod);  
}