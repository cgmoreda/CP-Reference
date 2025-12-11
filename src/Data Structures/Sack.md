```cpp
struct dsuOnTrees {
  dsuOnTrees(int n, vector<vector<int>> &adj) : n(n + 1), adj(adj) {
    cnt = size = st = vector<int>(n + 1);
    ver.push_back(0);
    timer = 1;
    pre(1, -1);
    dfs(1, -1, 0);
  }
  int n, timer;
  vector<int> cnt, size, st, ver;
  vector<vector<int>> adj;
  void pre(int node, int par) {
    size[node] = 1;
    st[node] = timer++;
    ver.push_back(node);
    for (auto it : adj[node]) {
      if (it == par)
        continue;
      pre(it, node);
      size[node] += size[it];
    }
  }
  void dfs(int v, int p, bool keep) {
    int mx = -1, bigChild = -1;
    for (auto u : adj[v])
      if (u != p && size[u] > mx)
        mx = size[u], bigChild = u;
    for (auto u : adj[v])
      if (u != p && u != bigChild)
        dfs(u, v, 0); // run a dfs on small childs and clear them from cnt

    if (bigChild != -1)
      dfs(bigChild, v, 1); // bigChild marked as big and not cleared from cnt

    for (auto u : adj[v])
      if (u != p && u != bigChild)
        for (int p = st[u]; p < st[u] + size[u]; p++) {
          int node = ver[p];
          // calc - merge between small subtrees and bigchild subtree
          // insert into global datastructure
        }
    // insert v into to global datastructure
    // now subtree v is inserted into global data structure

    if (keep == 0)
      for (int p = st[v]; p < st[v] + size[v]; p++)
        for (auto it : ask[ver[p]]) {
          int node = ver[p];
          // remove from global datastructure
        }
  }
};
```