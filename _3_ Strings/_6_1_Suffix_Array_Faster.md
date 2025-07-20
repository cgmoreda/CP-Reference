```cpp
class suffix_array {  
    const static int alpha = 128;  
    int getOrder(int a) const {  
        return (a < (int) order.size() ? order[a] : 0);  
    }  
public:  
    int n;  
    string s;  
    vector<int> suf, order, lcp; // order store position of suffix i in suf array  
    suffix_array(const string &s) : n(s.size() + 1), s(s) {  
        suf = order = lcp = vector<int>(n);  
        vector<int> bucket_idx(n), newOrder(n), newsuff(n);  
        vector<int> prev(n), head(alpha, -1);  
          
        for (int i = 0; i < n; i++) {  
            prev[i] = head[s[i]];  
            head[s[i]] = i;  
        }  
        int buc = -1, idx = 0;  
        for (int i = 0; i < alpha; i++) {  
            if (head[i] == -1) continue;  
            bucket_idx[++buc] = idx;  
            for (int j = head[i]; ~j; j = prev[j])  
                suf[idx++] = j, order[j] = buc;  
        }  
        int len = 1;  
        do {  
            auto cmp = [&](int a, int b) {  
                if (order[a] != order[b])  
                    return order[a] < order[b];  
                return getOrder(a + len) < getOrder(b + len);  
            };  
            for (int i = 0; i < n; i++) {  
                int j = suf[i] - len;  
                if (j < 0)  
                    continue;  
                newsuff[bucket_idx[order[j]]++] = j;  
            }  
            for (int i = 1; i < n; i++) {  
                suf[i] = newsuff[i];  
                bool cmpres = cmp(suf[i - 1], suf[i]);  
                newOrder[suf[i]] = newOrder[suf[i - 1]] + cmpres;  
                if (cmpres)  
                    bucket_idx[newOrder[suf[i]]] = i;  
            }  
            order = newOrder;  
            len <<= 1;  
        } while (order[suf[n - 1]] != n - 1);  
    }  
};
```