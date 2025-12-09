```cpp
// don't forget defaulf construct in node
struct HLD {
  int n;
  vector<int> par, depth, heavy, head, cnt, pos_array, pos_node, val, edge_node;
  vector<vector<int>> adj;
  bool value_on_edge = false;
  segment_tree<node> seg;
  HLD(int n, vector<int> &val, vector<vector<int>> &adj) : n(n), adj(adj) {
    init(val);
  }
  void init(vector<int> &val) {
    depth = head = cnt = pos_array = pos_node = vector<int>(n + 1);
    heavy = par = vector<int>(n + 1, -1);
    this->val = val;
    decompose(1);
  }
  HLD(int n, vector<vector<array<int, 3>>> &adj) : n(n) {
    vector<int> val(n + 1);
    value_on_edge = true;
    this->adj = vector<vector<int>>(n + 1);
    this->edge_node = vector<int>(n + 1);
    auto direct_edge = [&](auto &self, int u, int p) -> void {
      for (auto &[v, w, idx] : adj[u]) {
        if (v == p)
          continue;
        edge_node[idx] = v;
        this->adj[u].push_back(v);
        val[v] = w;
        self(self, v, u);
      }
    };
    direct_edge(direct_edge, 1, -1);
    init(val);
  }
  void dfs_hld(int u) {
    cnt[u] = 1;
    int max_size = 0;
    for (auto v : adj[u]) {
      if (v == par[u])
        continue;
      par[v] = u;
      depth[v] = depth[u] + 1;
      dfs_hld(v);
      cnt[u] += cnt[v];
      if (max_size < cnt[v]) {
        max_size = cnt[v];
        heavy[u] = v;
      }
    }
  }
  void decompose(int root = 1) {
    dfs_hld(root);
    // 1-based
    int nxt = 1;
    for (int chain_root = 1, pos = 1; chain_root <= n; chain_root++) {
      if (par[chain_root] == -1 || heavy[par[chain_root]] != chain_root) {
        for (int ch = chain_root; ~ch; ch = heavy[ch]) {
          head[ch] = chain_root;
          pos_array[ch] = nxt;
          pos_node[nxt++] = ch;
        }
      }
    }
    // --> build segment tree
    seg = segment_tree<node>(n + 1);
    for (int u = 1; u <= n; u++) {
      seg.update(pos_array[u], val[u]);
    }
  }
  node query(int u, int v) {
    struct Seg {
      int l, r;
      bool rev;
    };
    vector<Seg> left, right;
    while (head[u] != head[v]) {
      if (depth[head[u]] >= depth[head[v]]) {
        left.push_back({pos_array[head[u]], pos_array[u], true});
        u = par[head[u]];
      } else {
        right.push_back({pos_array[head[v]], pos_array[v], false});
        v = par[head[v]];
      }
    }
    if (depth[u] >= depth[v]) {
      int l = pos_array[v] + value_on_edge;
      int r = pos_array[u];
      if (l <= r)
        left.push_back({l, r, true});
    } else {
      int l = pos_array[u] + value_on_edge;
      int r = pos_array[v];
      if (l <= r)
        right.push_back({l, r, false});
    }

    vector<Seg> segs;
    for (auto &s : left)
      segs.push_back(s);
    reverse(right.begin(), right.end());
    for (auto &s : right)
      segs.push_back(s);

    //---> default node
    // if order is important check rev and edit reverse cur
    node ans(0);
    for (auto &[l, r, rev] : segs) {
      node cur = seg.query(l, r);
      ans = seg.merge(ans, cur);
    }
    return ans;
  }

  void update(int u, int c) { seg.update(pos_array[u], c); }

  void update_edge(int edge_idx, int c) { update(edge_node[edge_idx], c); }
};
```