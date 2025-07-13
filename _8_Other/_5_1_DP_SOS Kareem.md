```cpp
const int LG = 22;
const int M = 1 << LG;
```

// subset contribute to its superset
```cpp
void forward1(vector<ll>&dp) {
    for (int bt = 0; bt < LG; ++bt) {
        for (int m = 0; m < M; ++m) {
            if (m >> bt & 1){
                dp[m] += dp[m ^ (1 << bt)];
            }
        }
    }
}
```

// superset contribute to its subset
```cpp
void forward2(vector<ll>&dp) {
    for (int bt = 0; bt < LG; ++bt) {
        for (int m = M - 1; m >= 0; m--) {
            if (m >> bt &1){
                dp[m ^ (1 << bt)] += dp[m];
            }
        }
    }
}
```

// remove subset contribution from superset
```cpp
void backward1(vector<ll>&dp) {
    for (int bt = 0; bt < LG; bt++){
        for (int m = M - 1; m >= 0; m--){
            if (m >> bt &1){
                dp[m] -= dp[m ^ (1 << bt)];
            }
        }
    }
}
```

// remove superset contribution from subset
```cpp
void backward2(vector<ll> &dp) {
    for (int bt = 0; bt < LG; bt++){
        for (int m = 0; m < M; m++){
            if (m >> bt &1){
                dp[m ^ (1 << bt)] -= dp[m];
            }
        }
    }
}
```