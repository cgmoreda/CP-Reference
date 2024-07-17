//return sum of sequence a, a+x , a+2x .... b  
ll sumSequence(ll a, ll b, ll x) {  
    a = ((a + x - 1) / x) * x;  
    b = (b / x) * x;  
    return (b + a) * (b - a + x) / (2 * x);  
}