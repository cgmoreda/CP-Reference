struct SuffixArray {
    const static int alpha = 128, LOG = 20;
    vector<int> suf, order, newOrder, lcp, logs;
    vector<vector<int>> table;
    string s;
    int n;

    SuffixArray(const string& _s) : n(sz(_s) + 1), s(_s) {
        s += ' ';
        suf = order = newOrder = vector<int>(n);
        vector<int> bucket_idx(n), newOrder(n), new_suf(n);
        vector<int> prev(n), head(alpha, -1);

        auto getOrder = [&](const int& a) -> int {
            return a < n ? order[a] : 0;
        };

        for (int i = 0; i < n; i++) {
            prev[i] = head[s[i]];
            head[s[i]] = i;
        }
        for (int i = 0, buc = -1, idx = 0; i < alpha; i++) {
            if(head[i] == -1) continue;
            bucket_idx[++buc] = idx;
            for (int j = head[i]; ~j; j = prev[j]){
                suf[idx++] = j; order[j] = buc;
            }
        }

        for (int len = 1; order[suf[n - 1]] != n - 1; len <<= 1) {
            auto comp = [&](const int &a, const int &b) -> bool {
                if (order[a] != order[b]) return order[a] < order[b];
                return getOrder(a + len) < getOrder(b + len);
            };
            for (int i = 0; i < n; i++) {
                int j = suf[i] - len;
                if(j < 0) continue;
                new_suf[bucket_idx[order[j]]++] = j;
            }
            for(int i = 1; i < n; i++){
                suf[i] = new_suf[i];
                bool newGroup = comp(suf[i - 1], suf[i]);
                newOrder[suf[i]] = newOrder[suf[i - 1]] + newGroup;
                if(newGroup){
                    bucket_idx[newOrder[suf[i]]] = i;
                }
            }
            order = newOrder;
        }

        lcp = vector<int>(n);
        int k = 0;
        for (int i = 0; i < n - 1; i++) {
            int pos = order[i];
            int j = suf[pos - 1];
            while (s[i + k] == s[j + k]) k++;
            lcp[pos] = k;
            k = max(0, k - 1);
        }
        buildTable();
    }

    void buildTable() {
        table = vector<vector<int>>(n + 1, vector<int>(LOG));
        logs = vector<int>(n + 1);
        logs[1] = 0;
        for (int i = 2; i <= n; i++)
            logs[i] = logs[i >> 1] + 1;
        for (int i = 0; i < n; i++) {
            table[i][0] = lcp[i];
        }
        for (int j = 1; j <= logs[n]; j++) {
            for (int i = 0; i <= n - (1 << j); i++) {
                table[i][j] = min(table[i][j - 1], table[i + (1 << (j - 1))][j - 1]);
            }
        }
    }

    int LCP(int i, int j) {
        if (i == j) return n - i - 1;
        int l = order[i], r = order[j];
        if (l > r) swap(l, r);
        l++;
        int sz = logs[r - l + 1];
        return min(table[l][sz], table[r - (1 << sz) + 1][sz]);
    }

    int LCP_Order(int l, int r){
        if (l == r) return n-suf[l]-1;
        if (l > r) swap(l, r);
        l++;
        int sz = logs[r - l + 1];
        return min(table[l][sz], table[r - (1 << sz) + 1][sz]);

    }

    int compare_substrings(int l1, int r1, int l2, int r2) {
        int k = min({LCP(l1, l2), r1 - l1 + 1, r2 - l2 + 1});
        l1 += k; l2 += k;
        if (l1 > r1 && l2 > r2) return 0;
        if (l1 > r1) return -1;
        if (l2 > r2) return 1;
        return (s[l1] > s[l2] ? 1 : -1);
    }
};