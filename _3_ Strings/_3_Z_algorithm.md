```cpp
/* z[i] equal the length of the longest substring starting from s[i]  
 which is also a prefix of s */
 vector<int> z_algo(string s) {  
    int n = s.size();  
    vector<int> z(n);  
    z[0] = n;  
    for (int i = 1, L = 1, R = 1; i < n; i++) {  
        int k = i - L;  
        if (z[k] + i >= R) {  
            L = i;  
            R = max(R, i);  
            while (R < n && s[R - L] == s[R]) R++;  
            z[i] = R - L;  
        } else z[i] = z[k];  
    }  
    return z;  
}
```


```cpp
// z_function kareem
vector<int> z_function(const string&s){
    int n = s.size();
    vector<int>z(n);
    int l = 0,r = 0;
    for(int i =1;i<n;i++){
        if(i < r){
            z[i] = min(r - i,z[i - l]);
        }
        while(i + z[i] < n && s[i + z[i]] == s[z[i]])
            z[i]++;
        if(i + z[i] > r){
            l = i;
            r = i + z[i];
        }
    }
    return z;
}
```