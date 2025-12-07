Dinic with capacity scaling runs in:
O(V * E * log C)
where
* V = number of vertices
* E = number of edges
* C = maximum edge capacity.

```cpp
const ll inf = 1LL << 61;

struct Dinic {
    struct edge {
        int to, rev;
        ll flow, w;
        int id;
    };
    int n, s, t, mxid;
    vector<int> d, flow_through, done;
    vector<vector<edge>> g;

    Dinic() {}

    Dinic(int _n) {
        n = _n + 10;
        mxid = 0;
        g.resize(n);
    }

    void add_edge(int u, int v, ll w, int id = -1) {
        edge a = {v, (int)g[v].size(), 0, w, id};
        edge b = {u, (int)g[u].size(), 0, w, -2}; // for bidirectional edges cap(b) = w
        g[u].emplace_back(a);
        g[v].emplace_back(b);
        mxid = max(mxid, id);
    }

    bool bfs(ll scale) {
        d.assign(n, -1);
        d[s] = 0;
        queue<int> q;
        q.push(s);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (auto &e : g[u]) {
                int v = e.to;
                if (d[v] == -1 && e.flow < e.w && e.w >= scale) {
                    d[v] = d[u] + 1;
                    q.push(v);
                }
            }
        }
        return d[t] != -1;
    }

    ll dfs(int u, ll flow, ll scale) {
        if (u == t) return flow;
        for (int &i = done[u]; i < (int)g[u].size(); i++) {
            edge &e = g[u][i];
            if (e.w < scale || e.flow >= e.w) continue;
            int v = e.to;
            if (d[v] == d[u] + 1) {
                ll nw = dfs(v, min(flow, e.w - e.flow), scale);
                if (nw > 0) {
                    e.flow += nw;
                    g[v][e.rev].flow -= nw;
                    return nw;
                }
            }
        }
        return 0;
    }

    ll max_flow(int _s, int _t) {
        s = _s;
        t = _t;
        ll flow = 0;

        // Determine the maximum capacity in the graph
        ll scale = 1;
        for (int i = 0; i < n; i++) {
            for (const auto &e : g[i]) {
                scale = max(scale, e.w);
            }
        }

        // Apply scaling
        for (scale = (scale + 1) / 2; scale > 0; scale /= 2) {
            while (bfs(scale)) {
                done.assign(n, 0);
                while (ll nw = dfs(s, inf, scale)) flow += nw;
            }
        }

        flow_through.assign(mxid + 10, 0);
        for (int i = 0; i < n; i++) 
            for (auto e : g[i]) 
                if (e.id >= 0) 
                    flow_through[e.id] = e.flow;

        return flow;
    }
};
```