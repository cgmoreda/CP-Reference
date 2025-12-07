```cpp
  
struct Node {  
  Node *ls{}, *rs{};  
  int sum{};  
} pool[int(1e6)];  
  
int top;  
Node *null = pool + 0;  
  
void reset() {  
  top = 1;  
  null->sum = 0;  
  null->ls = null->rs = null;  
}  
  
Node *newNode() {  
  auto p = pool + (top++);  
  *p = *null;  
  return p;  
}  
  
// x is postion to insert  
Node *add(Node *p, int l, int r, int x) {  
  auto np = newNode();  
  *np = *p;  
  np->sum++;  
  if (r - l == 1) {  
    return np;  
  }  
  int m = (l + r) / 2;  
  if (x < m) {  
    np->ls = add(p->ls, l, m, x);  
  } else {  
    np->rs = add(p->rs, m, r, x);  
  }  
  return np;  
}  
  
void solve() {  
  int n;  
  const int C = (int)1E5;  
  vector<Node *> root(n);  
  
  // when add, w is postion on seg you want to add  
  // root[v] = add(root[u], 1, C + 1, w);  auto Find = [&](Node *a, Node *b, int k) {  
    int l = 1, r = C + 1;    while (r - l > 1) {      int m = (l + r) / 2;      int cnt = a->ls->sum - b->ls->sum;      if (cnt >= k) {        a = a->ls;        b = b->ls;        r = m;      } else {        k -= cnt;        a = a->rs;        b = b->rs;        l = m;      }    }    return l;  };  
}
```