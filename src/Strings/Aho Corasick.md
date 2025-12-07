```cpp
struct aho_corasick{  
    struct trie_node {  
          
        vector<int> pIdxs; //probably take memory limit  
        map<char, int> next;  
        int fail;  
        trie_node() : fail(0) {}  
        bool have_next(char ch) {  
            return next.find(ch) != next.end();  
        }  
        int &operator[](char ch) {  
            return next[ch];  
        }  
    };  
    vector<trie_node> t;  
    vector<string> patterns;  
    vector<int> end_of_pattern;  
    vector<vector<int>> adj;  
    int insert(const string &s, int patternIdx) {  
        int root = 0;  
        for (const char &ch: s) {  
            if (!t[root].have_next(ch)) {  
                t.push_back(trie_node());  
                t[root][ch] = t.size() - 1;  
            }  
            root = t[root][ch];  
        }  
        t[root].pIdxs.push_back(patternIdx);  
        return root;  
    }  
    int next_state(int cur, char ch) {  
        while (cur > 0 && !t[cur].have_next(ch))  
            cur = t[cur].fail;  
        if (t[cur].have_next(ch))  
            return t[cur][ch];  
        return 0;  
    }  
    void buildAhoTree() {  
        queue<int> q;  
        for (auto &child: t[0].next)  
            q.push(child.second);  
        while (!q.empty()) {  
              
            int cur = q.front();  
            q.pop();  
            for (auto &child: t[cur].next) {  
                int k = next_state(t[cur].fail, child.first);  
                t[child.second].fail = k;  
                vector<int> &idxs = t[child.second].pIdxs;  
                //dp[child.second] = max(dp[child.second],dp[k]);  
                idxs.insert(idxs.end(), all(t[k].pIdxs));  
                q.push(child.second);  
            }  
        }  
    }  
    void buildFailureTree() {  
        adj = vector<vector<int>>(t.size());  
        for (int i = 1; i < t.size(); i++)  
            adj[t[i].fail].push_back(i);  
    }  
    aho_corasick(const vector<string> &_patterns) {  
        t.push_back(trie_node());  
        patterns = _patterns;  
        end_of_pattern = vector<int>(patterns.size());  
        for (int i = 0; i < patterns.size(); i++)  
            end_of_pattern[i] = insert(patterns[i], i);  
        buildAhoTree();  
        //buildFailureTree();  
    }  
    vector<vector<int>> match(const string &str) {  
        int k = 0;  
        vector<vector<int>> rt(patterns.size());  
        for (int i = 0; i < str.size(); i++) {  
            k = next_state(k, str[i]);  
            for (auto &it: t[k].pIdxs)  
                rt[it].push_back(i);  
        }  
        return rt;  
    }  
};
```