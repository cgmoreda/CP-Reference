```cpp

const int LOG = 21;
struct Basis {
    int basis[LOG];
    int lst_idx[LOG];
    int sz;
 
    Basis() {
        sz = 0;
        for (int i = LOG - 1; i >= 0; --i) {
            basis[i] = 0;
            lst_idx[i] = -1;
        }
    }
    void insert(int x, int idx) {
        for (int i = LOG - 1; i >= 0; --i) {
            if ((x & (1ll << i)) == 0) continue;
            if(lst_idx[i] < idx)
            {
                swap(x, basis[i]);
                swap(lst_idx[i], idx);
                ++sz;
            }
            x ^= basis[i];
        }
    }
    int get_max(int l) {
        int ans = 0;
        for (int i = LOG - 1; i >= 0; --i) {
            if(basis[i] && !(ans & (1ll<<i)) && lst_idx[i] >= l)
                ans ^= basis[i];
        }
        return ans;
    }
};
 
void solve()
{
 
    Basis B = Basis();
    int n; cin >> n;
    vector<Basis> arr(n);
    for (int i = 0; i < n; ++i) {
        int x; cin >> x;
        B.insert(x, i);
        arr[i] = B;
    }
 
    int q; cin >> q;
    while (q--)
    {
        int l, r; cin >> l >> r;
        l--, r--;
        cout << arr[r].get_max(l) << endl;
    }
 
}
```
