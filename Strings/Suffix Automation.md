```cpp
struct suffix_automaton {  
    struct state {  
        int len, link = 0, cnt = 0;  
        bool terminal = false, is_clone = false;  
        map<char, int> next;  
        state(int len = 0) : len(len) {}  
        bool have_next(char ch) {  
            return next.find(ch) != next.end();  
        }  
        void clone(const state &other, int nlen) {  
            len = nlen;  
            next = other.next;  
            link = other.link;  
            is_clone = true;  
        }  
    };  
    vector<state> st;  
    int last = 0;  
    suffix_automaton() {  
        st.push_back(state());  
        st[0].link = -1;  
    }  
    suffix_automaton(const string &s) : suffix_automaton() {  
        for (char ch: s)  
            extend(ch);  
        for (int cur = last; cur > 0; cur = st[cur].link)  
            st[cur].terminal = true;  
    }  
    void extend(char c) {  
          
        int cur = st.size();  
        st.push_back(state(st[last].len + 1));  
        st[cur].cnt = 1;  
        int p = last;  
        last = cur;  
        while (p != -1 && !st[p].have_next(c)) {  
            st[p].next[c] = cur;  
            p = st[p].link;  
        }  
        if (p == -1)  
            return;  
        int q = st[p].next[c];  
        if (st[p].len + 1 == st[q].len) {  
            st[cur].link = q;  
            return;  
        }  
        int clone = st.size();  
        st.push_back(state());  
        st[clone].clone(st[q], st[p].len + 1);  
        while (p != -1 && st[p].next[c] == q) {  
            st[p].next[c] = clone;  
            p = st[p].link;  
        }  
        st[q].link = st[cur].link = clone;  
    }  
    void calc_number_of_occurrences() {  
        vector<vector<int>> lvl(st[last].len + 1);  
        for (int i = 1; i < st.size(); i++)  
            lvl[st[i].len].push_back(i);  
        for (int i = st[last].len; i >= 0; i--)  
            for (auto cur: lvl[i])  
                st[st[cur].link].cnt += st[cur].cnt;  
    }  
    vector<ll> dp;  
    ll Count(int cur) //count number of paths  
    {  
        ll &rt = dp[cur];  
        if (rt)  
            return rt;  
        rt = 1;  
        for (auto ch: st[cur].next)  
            rt += Count(ch.second);  
        return rt;  
          
    }  
    string kth_substring(ll k) //1-based,different substring,0 = ""  
    {  
        assert(k <= Count(0));  
        string rt;  
        int cur = 0;  
        while (k > 0) {  
            for (auto ch: st[cur].next) {  
                if (Count(ch.second) < k)  
                    k -= Count(ch.second);  
                else {  
                    rt += ch.first;  
                    cur = ch.second;  
                    k--;  
                    break;  
                }  
            }  
        }  
        return rt;  
    }  
    string longest_common_substring(const string &t) {  
        int cur = 0, l = 0, mx = 0, idx = 0;  
        for (int i = 0; i < t.size(); i++) {  
            while (cur > 0 && !st[cur].have_next(t[i])) {  
                cur = st[cur].link;  
                l = st[cur].len;  
            }  
            if (st[cur].have_next(t[i])) {  
                cur = st[cur].next[t[i]];  
                l++;  
            }  
            if (l > mx) {  
                mx = l;  
                idx = i;  
            }  
        }  
        return t.substr(idx - mx + 1, mx);  
    }  
};
```