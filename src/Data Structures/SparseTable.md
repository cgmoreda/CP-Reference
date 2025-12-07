```cpp
template<typename T>
struct sparseTable {
    vector<vector<T>> table;
    vector<int> lg;
    int n, maxLog;
    sparseTable(vector<ll> &v) {
        n = v.size();
        lg.resize(n + 1);
        for (int i = 2; i <= n; ++i)lg[i] = lg[i / 2] + 1;
        maxLog = lg[n] + 1;
        table.resize(n, vector<T>(maxLog));
        for (int i = 0; i < n; i++) {
            table[i][0] = v[i];
        }
        for (int j = 1; j < maxLog; j++) {
            for (int i = 0; i <= n - (1 << j); i++) {
                table[i][j] = min(table[i][j - 1], table[i + (1 << (j - 1))][j - 1]);
            }
        }
    }
    T query(int l, int r) {
        assert(l <= r);
        int j = lg[r - l + 1];
        return min(table[l][j], table[r - (1 << j) + 1][j]);
    }
    T query2(int l, int r) {
        T mn = 2e9;
        for (int i = maxLog; i >= 0; i--) {
            if ((1 << i) <= r - l + 1) {
                mn = min(mn, table[l][i]);
                l += 1 << i;
            }
        }
        return mn;
    }
};
```