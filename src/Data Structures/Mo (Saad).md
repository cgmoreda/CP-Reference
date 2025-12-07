```cpp
  
const int N = 1e5 + 5;  
vector<int> v(N);  
int root;  
struct query {  
  int l, r, idx;  
  bool operator<(query& oth) const {  
    if (l / root == oth.l / root) return r < oth.r;  
    return l < oth.l;  
  }  
};  
vector<query> ask;  
vector<ll> ans(N);  
ll cur;  
int n, q, l = 0, r = -1;  
struct MO {  
  void add(int idx) {}  
  void remove(int idx) {}  
  void change(int idx) {  
    while (r < ask[idx].r) {  
      r++;  
      add(r);  
    }  
    while (r > ask[idx].r) {  
      remove(r);  
      r--;  
    }  
    while (l > ask[idx].l) {  
      l--;  
      add(l);  
    }  
    while (l < ask[idx].l) {  
      remove(l);  
      l++;  
    }  
    ans[ask[idx].idx] = cur;  
  }  
};  
void solve() {  
  cin >> n >> q;  
  ask = vector<query>(q);  
  root = sqrt(q) + 1;  
  for (int i = 0; i < n; i++) cin >> v[i];  
  for (int i = 0; i < q; i++)  
    cin >> ask[i].l >> ask[i].r, --ask[i].l, --ask[i].r, ask[i].idx = i;  
  sort(all(ask));  
  MO mo;  
  for (int i = 0; i < q; i++) mo.change(i);  
  for (int i = 0; i < q; i++) cout << ans[i] << endl;  
}
```