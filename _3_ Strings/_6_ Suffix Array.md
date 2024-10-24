class suffix_array {  
    int getOrder(int a) const {  
        return (a < (int) order.size() ? order[a] : 0);  
    }  
  
    void radix_sort(int k) {  
        vector<int> frq(n), tmp(n);  
        for (auto &it: suf)  
            frq[getOrder(it + k)]++;  
        for (int i = 1; i < n; i++)  
            frq[i] += frq[i - 1];  
        for (int i = n - 1; i >= 0; i--)  
            tmp[--frq[getOrder(suf[i] + k)]] = suf[i];  
        suf = tmp;  
    }  
  
public:  
    int n;  
    string s;  
    vector<int> suf, lcp, order; // order store position of suffix i in suf array  
    suffix_array(const string &s) :  
            n(s.size() + 1), s(s) {  
        suf = order = vector<int>(n);  
        vector<int> newOrder(n);  
        for (int i = 0; i < n; i++)  
            suf[i] = i;  
        { //sort according to first character  
            vector<int> tmp(n);  
            for (int i = 0; i < n; i++)  
                tmp[i] = s[i];  
            sort(all(tmp));  
            for (int i = 0; i < n; i++)  
                order[i] = (lower_bound(all(tmp), s[i]) - tmp.begin());  
        }  
        for (int len = 1; newOrder.back() != n - 1; len <<= 1) {  
            auto cmp = [&](const int &a, const int &b) {  
                if (order[a] != order[b])  
                    return order[a] < order[b];  
                return getOrder(a + len) < getOrder(b + len);  
            };  
            //sort(all(suf), cmp); //run in 576ms (n<=4e5)  
            radix_sort(len); //sort second part  
            radix_sort(0); //sort first part  
            newOrder[0] = 0;  
            for (int i = 1; i < n; i++)  
                newOrder[i] = newOrder[i - 1] + cmp(suf[i - 1], suf[i]);  
            for (int i = 0; i < n; i++)  
                order[suf[i]] = newOrder[i];  
        }  
        buildLCP();  
    }  
  
    /*  
    * longest common prefix    * O(n)    * lcp[i] = lcp(suf[i],suf[i-1])    */    void buildLCP() {  
        lcp = vector<int>(n);  
        int k = 0;  
        for (int i = 0; i < n - 1; i++) {  
            int pos = order[i];  
            int j = suf[pos - 1];  
            while (s[i + k] == s[j + k])  
                k++;  
            lcp[pos] = k;  
            if (k)  
                k--;  
        }  
    }  
  
    int LCP_by_order(int a, int b) {  
        if (a > b) swap(a, b);  
        int mn = n - suf[a] - 1;  
        for (int k = a + 1; k <= b; k++)  
            mn = min(mn, lcp[k]);  
        return mn;  
    }  
  
    //LCP(i,j) : longest common prefix between suffix i and suffix j  
    int LCP(int i, int j) {  
        //return LCP_by_order(order[i],order[j]);  
        if (order[j] < order[i])  
            swap(i, j);  
        int mn = n - i - 1;  
        for (int k = order[i] + 1; k <= order[j]; k++)  
            mn = min(mn, lcp[k]);  
        return mn;  
    }  
  
    //compare s[a.first..a.second] with s[b.first..b.second]  
    //-1:a<b ,0:a==b,1:a>b    int compare_substrings(pair<int, int> a, pair<int, int> b) {  
        int lcp = min({LCP(a.first, b.first), a.second - a.first + 1,  
                       b.second - b.first + 1});  
        a.first += lcp;  
        b.first += lcp;  
        if (a.first <= a.second) {  
            if (b.first <= b.second) {  
                if (s[a.first] == s[b.first])  
                    return 0;  
                return (s[a.first] < s[b.first] ? -1 : 1);  
            }  
            return 1;  
        }  
        return (b.first <= b.second ? -1 : 0);  
    }  
  
    pair<int, int> find_string(const string &x) {  
        int st = 0, ed = n;  
        for (int i = 0; i < sz(x) && st < ed; i++) {  
            auto cmp = [&](int a, int b) {  
                if (a == -1)  
                    return x[i] < s[b + i];  
                return s[a + i] < x[i];  
            };  
            st = lower_bound(suf.begin() + st, suf.begin() + ed, -1, cmp)  
                 - suf.begin();  
            ed = upper_bound(suf.begin() + st, suf.begin() + ed, -1, cmp)  
                 - suf.begin();  
        }  
        return {st, ed - 1};  
    }  
};  
  
ll number_of_different_substrings(string s) {  
    int n = s.size();  
    suffix_array sa(s);  
    ll cnt = 0;  
    for (int i = 0; i <= n; i++)  
        cnt += n - sa.suf[i] - sa.lcp[i];  
    return cnt;  
}  
  
string longest_common_substring(const string &s1, const string &s2) {  
    suffix_array sa(s1 + "#" + s2);  
    vector<int> suf = sa.suf, lcp = sa.lcp;  
    auto type = [&](int idx) {  
        return idx <= s1.size();  
    };  
    int mx = 0, idx = 0;  
    int len = s1.size() + 1 + s2.size();  
    for (int i = 1; i <= len; i++)  
        if (type(suf[i - 1]) != type(suf[i]) && lcp[i] > mx) {  
            mx = lcp[i];  
            idx = min(suf[i - 1], suf[i]);  
        }  
    return s1.substr(idx, mx);  
}  
  
int longest_common_substring(const vector<string> &v) {  
    int n = v.size();  
    int len = n - 1;  
    for (auto &it: v)  
        len += it.size();  
    string s(len, '.');  
    vector<int> type(len + 1, n), frq(n + 1);  
    for (int i = 0, j = 0; i < v.size(); i++) {  
        if (i) s[j] = 'z' + i; //review this  
        for (char ch: v[i]) {  
            s[j] = ch;  
            type[j] = i;  
            j++;  
        }  
    }  
    suffix_array sa(s);  
    60  
    vector<int> suf = sa.suf, lcp = sa.lcp;  
    monoqueue q;  
    int st = 0, ed = 0, cnt = 0, mx = 0;  
    while (st <= s.size()) {  
        while (ed <= s.size() && cnt < v.size()) {  
            q.push(lcp[ed], ed);  
            if (++frq[type[suf[ed]]] == 1)  
                cnt++;  
            ed++;  
        }  
        q.pop(st);  
        if (cnt == v.size()) mx = max(mx, q.getMin()); //st+1,ed  
        if (--frq[type[suf[st]]] == 0) cnt--;  
        st++;  
    }  
    return mx;  
}  
  
string kth_substring(string s, int k) { //1-based,repated  
    int n = s.size();  
    suffix_array sa(s);  
    vector<int> suf = sa.suf, lcp = sa.lcp;  
    for (int i = 1; i <= n; i++) {  
        int len = n - suf[i];  
        int cnt = 0;  
        for (int l = 1; l <= len; l++) {  
            cnt++;  
            int st = i + 1, ed = n, ans = i;  
            while (st <= ed) {  
                int md = st + ed >> 1;  
                if (sa.LCP_by_order(i, md) >= l)  
                    st = md + 1, ans = md;  
                else ed = md - 1;  
            }  
            cnt += ans - i;  
            if (cnt >= k) return s.substr(suf[i], l);  
        }  
        k -= len;  
    }  
    assert(0);  
}