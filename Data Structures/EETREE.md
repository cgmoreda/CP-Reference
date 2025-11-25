```cpp
/* @brief Palindromes in Dequeby adamant*/  
#define PROBLEM "https://judge.yosupo.jp/problem/palindromes_in_deque"  
#pragma GCC optimize("Ofast,unroll-loops")  
#pragma GCC target("tune=native")  
#include <bits/stdc++.h>  
using namespace std;  
  
template<int sigma = 26, char mch = 'a'>  
struct eertree {  
    eertree(size_t q) {  
        q += 2;  
        cnt = len = par = qlink = vector(q, 0);  
        to.resize(q);  
        link.resize(q);  
        ranges::fill(link[0], 1);  
        qlink[0] = 1;  
        len[1] = -1;  
    }  
  
    template<bool back = 1>  
    static int get(auto const &d, size_t idx) {  
        if (idx >= size(d)) { return -1; } else { return back ? rbegin(d)[idx] : d[idx]; }  
    }  
  
    template<bool back = 1>  
    static void push(auto &d, auto c) { back ? d.push_back(c) : d.push_front(c); }  
  
    template<bool back = 1>  
    static void pop(auto &d) { back ? d.pop_back() : d.pop_front(); }  
  
    template<bool back = 1>  
    void add_letter(char c) {  
        c -= mch;  
        push<back>(s, c);  
        int pre = get<back>(states, 0);  
        int last = make_to<back>(pre, c);  
        active += !(cnt[last]++);  
        int D = 2 + len[pre] - len[last];  
        while (D + len[pre] <= len[last]) {  
            pop<back>(states);  
            if (!empty(states)) {  
                pre = get<back>(states, 0);  
                D += get<back>(diffs, 0);  
                pop<back>(diffs);  
            } else { break; }  
        }  
        if (!empty(states)) { push<back>(diffs, D); }  
        push<back>(states, last);  
    }  
  
    template<bool back = 1>  
    void pop_letter() {  
        int last = get<back>(states, 0);  
        active -= !(--cnt[last]);  
        pop<back>(states);  
        pop<back>(s);  
        array cands = {pair{qlink[last], len[last] - len[qlink[last]]}, pair{par[last], 0}};  
        for (auto [state, diff]: cands) {  
            if (empty(states)) {  
                states = {state};  
                diffs = {diff};  
            } else {  
                int D = get<back>(diffs, 0) - diff;  
                int pre = get<back>(states, 0);  
                if (D + len[state] > len[pre]) {  
                    push<back>(states, state);  
                    pop<back>(diffs);  
                    push<back>(diffs, D);  
                    push<back>(diffs, diff);  
                }  
            }  
        }  
        pop<back>(diffs);  
    }  
  
    void add_letter(char c, bool back) { back ? add_letter<1>(c) : add_letter<0>(c); }  
    void pop_letter(bool back) { back ? pop_letter<1>() : pop_letter<0>(); }  
    int distinct() { return active; }  
  
    template<bool back = 1>  
    int maxlen() { return len[get<back>(states, 0)]; }  
  
private:  
    vector<array<int, sigma> > to, link;  
    vector<int> len, qlink, par, cnt;  
    deque<char> s;  
    deque<int> states = {0}, diffs;  
    int sz = 2, active = 0;  
  
    template<bool back = 1>  
    int make_to(int last, int c) {  
        if (c != get<back>(s, len[last] + 1)) { last = link[last][c]; }  
        if (!to[last][c]) {  
            int u = to[link[last][c]][c];  
            qlink[sz] = u;  
            link[sz] = link[u];  
            link[sz][get<back>(s, len[u])] = u;  
            len[sz] = len[last] + 2;  
            par[sz] = last;  
            to[last][c] = sz++;  
        }  
        return to[last][c];  
    }  
};  
  
void solve() {  
    int q;  
    cin >> q;  
    eertree me(q);  
    for (int i = 0; i < q; i++) {  
        int t;  
        cin >> t;  
        if (t / 2) { me.pop_letter(t % 2); } else {  
            char c;  
            cin >> c;  
            me.add_letter(c, t % 2);  
        }  
        cout << me.distinct() << ' ' << me.maxlen<0>() << ' ' << me.maxlen<1>() << "\n";  
    }  
}  
  
signed main() {  
    ios::sync_with_stdio(0);  
    cin.tie(0);  
    int t = 1;  
    while (t--) { solve(); }  
}
```