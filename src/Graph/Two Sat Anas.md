```cpp
  struct TwoSat {
  int n;
  SCC scc;
  vector<array<int, 2>> E;
  TwoSat(int n = 0) : n(n) {}
  inline int Not(int x) { return x ^ 1; }
  inline int Pos(int v) { return v << 1; }
  inline int Neg(int v) { return v << 1 ^ 1; }
  int addVar() { return n++; }

  void addImp(int u, int v) { E.push_back({u, v}); }
  void addOrEdge(int a, int b) {
    addImp(Not(a), b);
    addImp(Not(b), a);
  }
  void addXorEdge(int a, int b) {
    addOrEdge(a, b);
    addOrEdge(Not(a), Not(b));
  }
  void addEqualEdge(int a, int b) {
    addOrEdge(a, Not(b));
    addOrEdge(Not(a), b);
  }
  void forceValue(int a, int val) {
    if (val)
      addImp(Not(a), a);
    else
      addImp(a, Not(a));
  }

  void addAtMostOneLadder(const vector<int> &x) {
    if (sz(x) <= 1)
      return;
    int k = sz(x);
    vector<int> y(k−1);
    for (int i = 0; i < k− 1; i++) {
      y[i] = Pos(addVar());
    }
    addOrEdge(Not(x[0]), y[0]);
    for (int i = 1; i < k− 1; i++) {
      addOrEdge(Not(x[i]), y[i]);
      addOrEdge(Not(y[i− 1]), y[i]);
      addOrEdge(Not(x[i]), Not(y[i− 1]));
    }
    addOrEdge(Not(x[k− 1]), Not(y[k− 2]));
  }

  void buildGraph() {
    scc.init(n << 1);
    for (auto &[u, v] : E)
      scc.addEdge(u, v);
  }

  bool hasSolution() {
    buildGraph();
    scc.work();
    for (int i = 0; i < n; i++) {
      if (scc.compId[Pos(i)] == scc.compId[Neg(i)])
        return 0;
    }
    return 1;
  }

  vector<bool> build() {
    int C = scc.cntComp;
    vector<int> indeg(C), rk(C);
    for (int u = 0; u < C; u++) {
      for (int v : scc.dag[u]) {
        ++indeg[v];
      }
    }
    queue<int> q;
    for (int u = 0; u < C; u++) {
      if (!indeg[u])
        q.push(u);
    }
    for (int t = 0; !q.empty();) {
      int u = q.front();
      q.pop();
      rk[u] = t++;
      for (int v : scc.dag[u]) {
        if (−−indeg[v] == 0)
          q.push(v);
      }
    }

    vector<bool> ans(n);
    for (int i = 0; i < n; ++i)
      ans[i] = rk[scc.compId[Pos(i)]] > rk[scc.compId[Neg(i)]];
    return ans;
  }
};
```