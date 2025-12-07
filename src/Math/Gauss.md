```cpp
class Gauss {
    const int INF = 2;
    const double EPS = 1E-9;
public:
    int gauss(vector<vector<double> > a, vector<double> &ans) {
        int n = (int) a.size();
        int m = (int) a[0].size() - 1;

        vector<int> where(m, -1);
        for (int col = 0, row = 0; col < m && row < n; ++col) {
            int sel = row;
            for (int i = row; i < n; ++i)
                if (abs(a[i][col]) > abs(a[sel][col]))
                    sel = i;
            if (abs(a[sel][col]) < EPS)
                continue;
            for (int i = col; i <= m; ++i)
                swap(a[sel][i], a[row][i]);
            where[col] = row;

            for (int i = 0; i < n; ++i)
                if (i != row) {
                    double c = a[i][col] / a[row][col];
                    for (int j = col; j <= m; ++j)
                        a[i][j] -= a[row][j] * c;
                }
            ++row;
        }

        ans.assign(m, 0);
        for (int i = 0; i < m; ++i)
            if (where[i] != -1)
                ans[i] = a[where[i]][m] / a[where[i]][i];
        for (int i = 0; i < n; ++i) {
            double sum = 0;
            for (int j = 0; j < m; ++j)
                sum += ans[j] * a[i][j];
            if (abs(sum - a[i][m]) > EPS)
                return 0;
        }

        for (int i = 0; i < m; ++i)
            if (where[i] == -1)
                return INF;
        return 1;
    }

    int gaussWithMod(vector<vector<ll>> a, vector<ll> &ans, ll p) {
        int n = (int) a.size();
        int m = (int) a[0].size() - 1;

        vector<int> where(m, -1);
        for (int col = 0, row = 0; col < m && row < n; ++col) {
            int sel = row;
            for (int i = row; i < n; ++i)
                if (a[i][col] > a[sel][col])
                    sel = i;
            if (a[sel][col] == 0)
                continue;

            for (int i = col; i <= m; ++i)
                swap(a[sel][i], a[row][i]);
            where[col] = row;

            ll inv = modInverse(a[row][col], p);
            for (int i = 0; i < n; ++i) {
                if (i != row && a[i][col] != 0) {
                    ll c = a[i][col] * inv % p;
                    for (int j = col; j <= m; ++j) {
                        a[i][j] = (a[i][j] - a[row][j] * c % p + p) % p;
                    }
                }
            }
            ++row;
        }

        ans.assign(m, 0);
        for (int i = 0; i < m; ++i)
            if (where[i] != -1) {
                ll inv = modInverse(a[where[i]][i], p);
                ans[i] = (a[where[i]][m] * inv) % p;
            }


        for (int i = 0; i < n; ++i) {
            ll sum = 0;
            for (int j = 0; j < m; ++j)
                sum = (sum + ans[j] * a[i][j]) % p;
            if (sum != a[i][m])
                return 0; // No solution
        }

        for (int i = 0; i < m; ++i)
            if (where[i] == -1)
                return INF; // Infinite solutions

        return 1; // Unique solution
    }

    int gauss(vector<bitset<N>> a, int n, int m, bitset<N> &ans) {
        vector<int> where(m, -1);
        for (int col = 0, row = 0; col < m && row < n; ++col) {
            for (int i = row; i < n; ++i) {
                if (a[i][col]) {
                    swap(a[i], a[row]);
                    break;
                }
            }
            if (!a[row][col])
                continue;

            where[col] = row;

            for (int i = 0; i < n; ++i) {
                if (i != row && a[i][col])
                    a[i] ^= a[row];  // XOR the rows
            }
            ++row;
        }

        ans.reset();
        for (int i = 0; i < m; ++i)
            if (where[i] != -1)
                ans[i] = a[where[i]][m];

        for (int i = 0; i < n; ++i) {
            bool sum = 0;
            for (int j = 0; j < m; ++j)
                sum ^= (ans[j] & a[i][j]);  // XOR the known values
            if (sum != a[i][m])
                return 0;  // No solution
        }

        for (int i = 0; i < m; ++i)
            if (where[i] == -1)
                return INF;  // Infinite solutions

        return 1;  // Unique solution
    }

    int compute_rank(vector<vector<double>> A) {
        int n = A.size();
        int m = A[0].size();

        int rank = 0;
        vector<bool> row_selected(n, false);
        for (int i = 0; i < m; ++i) {
            int j;
            for (j = 0; j < n; ++j) {
                if (!row_selected[j] && abs(A[j][i]) > EPS)
                    break;
            }
            if (j != n) {
                ++rank;
                row_selected[j] = true;
                for (int p = i + 1; p < m; ++p)
                    A[j][p] /= A[j][i];
                for (int k = 0; k < n; ++k) {
                    if (k != j && abs(A[k][i]) > EPS) {
                        for (int p = i + 1; p < m; ++p)
                            A[k][p] -= A[j][p] * A[k][i];
                    }
                }
            }
        }
        return rank;
    }
};
```