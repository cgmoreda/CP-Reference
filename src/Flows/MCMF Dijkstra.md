```cpp
  struct MCMF {
  struct edge {
    int to, cap, flow;
    ll cost;
    int backEdge;
  };
  int n, src, sink;
  vector<vector<edge>> adj;
  vector<ll> pot, dis;
  vector<int> par, from_edge;

  MCMF(int n)
      : n(n), adj(n + 1), pot(n + 1), dis(n + 1), par(n + 1), from_edge(n) {}

  void addEdge(int u, int v, int cap, ll cost) {
    adj[u].push_back({v, cap, 0, cost, (int)adj[v].size()});
    adj[v].push_back({u, 0, 0,−cost, (int)adj[u].size()− 1});
  }

  bool dijkstra() {
    fill(dis.begin(), dis.end(), LLONG_MAX);
    fill(par.begin(), par.end(),−1);
    dis[src] = 0;
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>>
        pq;
    pq.emplace(0, src);
    while (!pq.empty()) {
      auto [d, u] = pq.top();
      pq.pop();
      if (d > dis[u])
        continue;
      for (int i = 0; i < (int)adj[u].size(); ++i) {
        edge &e = adj[u][i];
        if (e.flow == e.cap)
          continue;
        ll new_cost = e.cost + pot[u]− pot[e.to];
        if (dis[e.to] > dis[u] + new_cost) {
          dis[e.to] = dis[u] + new_cost;
          par[e.to] = u;
          from_edge[e.to] = i;
          pq.emplace(dis[e.to], e.to);
        }
      }
    }
    return dis[sink] != LLONG_MAX;
  }
  pair<int, ll> minCostMaxFlow(int _src, int _sink) {
    src = _src;
    sink = _sink;
    fill(pot.begin(), pot.end(), 0);
    int flow = 0;
    ll cost = 0;
    while (dijkstra()) {
      for (int i = 0; i <= n; ++i)
        if (dis[i] < LLONG_MAX)
          pot[i] += dis[i];
      int push = INT_MAX, cur = sink;
      while (cur != src) {
        int p = par[cur], e = from_edge[cur];
        push = min(push, adj[p][e].cap− adj[p][e].flow);
        cur = p;
      }
      cur = sink;
      while (cur != src) {
        int p = par[cur], e = from_edge[cur];
        adj[p][e].flow += push;
        adj[cur][adj[p][e].backEdge].flow− = push;
        cost += 1LL ∗ push ∗ adj[p][e].cost;
        cur = p;
      }
      flow += push;
    }
    return {flow, cost};
  }
};
```