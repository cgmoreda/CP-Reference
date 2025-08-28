segmented_sieve --> get primes in range ex(1e9:1e9+1e6) o[(r-l)*loglog(r)+ o(sieve)]
 rمتنساش تستخدم سيف قبله لحد جذر ال
```cpp
 const int N=1e5+5;
 bool composite[N];
void segmented_sieve()
{
	for(auto i:primes)
	{
		for(int j=max(i*i,(l+i-1)/i*i);j<=r;j+=i)
	     	composite[j-l]=1;                   // متسناش تنقص وانت بتسأل 
	}
	if(l==1)composite[0]=1;
}
```

//Linear Sieve  
```cpp
const int N = 1e7;  
int lpf[N + 1];  
vector<int> prime;  
  
void sieve() {  
    for (int i = 2; i <= N; i++) {  
        if (lpf[i] == 0) {  
            lpf[i] = i;  
            prime.push_back(i);  
        }  
        for (int j: prime) {  
            if (j > lpf[i] || 1LL * i * j > N)break;  
            lpf[i * j] = j;  
        }  
    }  
}
```