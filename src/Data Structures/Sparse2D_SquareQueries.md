```cpp
class Sparse2D_gcd {
private:
    vector<vector<vector<ll>>> dp;
public:
    ll merge(ll x, ll y) {
        return __gcd(x, y);
    }

    Sparse2D_gcd(const vector<vector<ll>> &a) {
        int n = a.size(), m = a[0].size();
        int LG = log2(min(n, m));
        dp = vector<vector<vector<ll>>>(n, vector<vector<ll>>(m, vector<ll>(LG+1)));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                dp[i][j][0] = a[i][j];
            }
        }
        for (int k = 1; k <= LG; k++) {
            int len = (1 << (k - 1));
            for (int i = 0; i + len < n; i++) {
                for (int j = 0; j + len < m; j++) {
                    int fi = dp[i][j][k - 1], se = dp[i][j + len][k - 1];
                    int fi2 = dp[i + len][j][k - 1], se2 = dp[i + len][j + len][k - 1];
                    dp[i][j][k] = merge(merge(fi, se), merge(fi2, se2));
                }
            }
        }
    }

    //return gcd of square (x,y) -> (x +k,y + k)
    ll query(int x, int y, int k) {
        int lg = log2(k);
        int fi = dp[x][y][lg], se = dp[x][y + k - (1 << lg)][lg], fi2 = dp[x + k - (1 << lg)][y][lg], 
            se2 = dp[(x + k -(1<< lg))][y + k - (1 << lg)][lg];
        return merge(merge(fi, se), merge(fi2, se2));
    }
};
```