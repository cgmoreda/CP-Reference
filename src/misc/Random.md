```cpp
-#include <random>  
  
static random_device rd;  
static mt19937 gen(rd());  
  
int randomgen(int x)  
{  
    uniform_int_distribution<> dis(0, x - 1);  
    int rndnum = dis(gen);  
    return rndnum;  
}
```

```cpp
#include <chrono>  
#include <random>  
  
//write this line once in top  
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count() *  
               ((uint64_t) new char | 1));  
  
// use this instead of rand()  
template<typename T>  
T Rand(T low, T high) {  
    return uniform_int_distribution<T>(low, high)(rng);  
}
```

```cpp
//shuffle array 
void solve() {
    int n;
    cin >> n;
    vector<int> ans(n);
    for (int i = 0; i < n; i++) {
        ans[i] = i + 1;
    }
    shuffle(ans.begin(), ans.end(), rng);
    //ans is shuffled
}
```