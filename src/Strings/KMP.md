```cpp
//KMP 
vector<int>KMP(const string&s){
    int n = sz(s);
    vector<int>fail(n);
    for(int i = 1;i<n;i++){
        int j = fail[i-1];
        while(j && s[i]!=s[j]){
            j = fail[j-1];
        }
        if(s[i] == s[j])j++;
        fail[i] = j;
    }
    return fail;
}
```