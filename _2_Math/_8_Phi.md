```cpp
const int N=1e6+5;
int phi[N];
void pre(){
    for (int i=0;i<N;i++)
        phi[i]=i;
    for (int i=2;i<N;i++){
        if (phi[i]==i){
            for (int j=i;j<N;j+=i)
                phi[j]-=phi[j]/i;
        }
    }

}
```

```cpp
ll phi(ll n){
    ll p_to_k, relative_primes=1;
    for (ll i=2,d=1;i*i<=n;i+=d,d=2){
        if (!(n%i)){
            p_to_k=1;
            while(!(n%i)){
                p_to_k*=i,n/=i;
            }
            relative_primes*=(p_to_k/i)*(i-1);

        }

    }
    if (n!=1){
        relative_primes*=(n-1);
    }
    return relative_primes;
}
```

```cpp
ll phi(ll n) {
    ll result = n;
    for (ll i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0)
                n /= i;
            result -= result / i;
        }
    }
    if (n > 1)
        result -= result / n;
    return result;
}
```