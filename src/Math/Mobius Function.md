```cpp
const int N = 2e6 + 10, MOD = 1e9 + 7;
char mob[N];
bool prime[N];
void moebius() {
	memset(mob, 1, sizeof mob);
	memset(prime + 2, 1, sizeof(prime) - 2);
	mob[0] = 0;
	mob[2] = -1;
	for (int i = 4; i < N; i += 2) {
		mob[i] *= (i & 3) ? -1 : 0;
		prime[i] = 0;
	}
	for (int i = 3; i < N; i += 2)
		if (prime[i]) {
			mob[i] = -1;
			for (int j = 2 * i; j < N; j += i) {
				mob[j] *= j % (1LL * i * i) ? -1 : 0;
				prime[j] = 0;
			}
		}
}
```

```cpp
  
const int N = 4e7 + 10;  
char mu[N];  
vector<bool> comp(N);  
  
void mobius_linear() {  
    vector<int> ps;  
    ps.reserve(N / 10);  
    mu[1] = 1;  
    for (int i = 2; i < N; ++i) mu[i] = 0; // optional, will be set  
  
    for (int i = 2; i < N; ++i) {  
        if (!comp[i]) {  
            ps.push_back(i);  
            mu[i] = -1;  
        }  
        for (int p: ps) {  
            long long v = 1LL * i * p;  
            if (v >= N) break;  
            comp[v] = true;  
            if (i % p == 0) {  
                mu[v] = 0;  
                break;  
            } // square divides  
            mu[v] = -mu[i];  
        }  
    }  
}

```