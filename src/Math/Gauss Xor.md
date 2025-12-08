```cpp
// problem link : https://codeforces.com/gym/101908/problem/M
const int N = 2005;

class Gauss {
    const int INF = 2;
    const double EPS = 1E-9;
public:
    //this code finds lexicographically largest solution
    //n is number of eq ,m is number of variables
    // xor gauss (mod 2)
    // x1 ^(not x2) ^(x3) = 1 -> (x1 ^(1 ^ x2) ^ x3 = 1)  (x1^x2^x3 = 0)
    int gauss(vector<bitset<N>> a, int n, int m, bitset<N> &ans) {
        vector<int> where(m, -1);
        // to make it minimum lexicographically Three Modifications
        // Modification 1: reverse col iteration ( left to right)
        for (int col = m - 1, row = 0; col >= 0 && row < n; col--) {
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
        //Modification 2: reverse i iteration (right to left)
        for (int i = 0; i < m; ++i) {
            if (where[i] != -1) {
                int r = where[i];
                bool sum = 0;
                for (int j = 0; j < i; ++j) {
                    sum ^= (a[r][j] & ans[j]);
                }
                ans[i] = (a[r][m] ^ sum);
            } else {
                // Modification 3 : if is free set it to 0
                ans[i] = 1;
            }
        }

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
};

void solve() {
    int n, m;
    cin >> n >> m;
    vector<bitset<N>> a(n);
    for (int i = 0; i < n; i++)a[i].set(m);
    cin.ignore();
    for (int i = 0; i < n; i++) {
        string s;
        getline(cin, s);
        s.pop_back();
        if (i + 1 < n) {
            s.pop_back();
            s.pop_back();
            s.pop_back();
            s.pop_back();
        }
        s.erase(s.begin());
        stringstream ss(s);
        while (ss >> s) {
            if (s == "or")continue;
            if (s == "not")a[i].flip(m);
            else {
                int num = stoi(s.substr(1)) - 1;
                a[i].flip(num);
            }
        }
    }

    Gauss gs;
    bitset<N> ans;
    int rt = gs.gauss(a, n, m, ans);
    if (rt == 0)cout << "impossible\n";
    else {
        for (int i = 0; i < m; i++) {
            if (ans[i])cout << "T";
            else cout << "F";
        }
        LL;
    }
}
```