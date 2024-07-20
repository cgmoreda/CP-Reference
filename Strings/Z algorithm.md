/* z[i] equal the length of the longest substring starting from s[i]  
 which is also a prefix of s */vector<int> z_algo(string s) {  
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