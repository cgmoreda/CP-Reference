int LIS(const vector<int> &v) {  
    vector<int> lis(v.size());//put value less than zero if needed  
    int l = 0;  
    for (int i = 0; i < sz(v); i++) {  
        int idx = lower_bound(lis.begin(), lis.begin() + l, v[i]) - lis.begin();  
        if (idx == l)  
            l++;  
        lis[idx] = v[i];  
    }  
    return l;  
}