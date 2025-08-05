```cpp
//Hopcroft-Karp algorithm for maximum bipartite matching
//O(sqrt(V) * E)
struct Hopcroft_Karp {//1-based
#define NIL 0
#define INF INT_MAX
	int n, m;``
	vector<vector<int>> adj;
	vector<int> rowAssign, colAssign, dist;
	bool bfs() {
		queue<int> q;
		dist = vector<int>(adj.size(), INF);
		for (int i = 1; i <= n; i++)
			if (rowAssign[i] == NIL) {
				dist[i] = 0;
				q.push(i);
			}
		while (!q.empty()) {
			int cur = q.front();
			q.pop();
			if (dist[cur] >= dist[NIL])break;
			for (auto& nxt : adj[cur]) {
				if (dist[colAssign[nxt]] == INF) {
					dist[colAssign[nxt]] = dist[cur] + 1;
					q.push(colAssign[nxt]);
				}
			}
		}
		return dist[NIL] != INF;
	}
	bool dfs(int i) {
		if (i == NIL)
			return true;
		for (int j : adj[i]) {
			if (dist[colAssign[j]] == dist[i] + 1 && dfs(colAssign[j])) {
				colAssign[j] = i;
				rowAssign[i] = j;
				return true;
			}
		}
		dist[i] = INF;
		return false;
	}
	Hopcroft_Karp(int n, int m)
		:n(n), m(m), adj(n + 1), rowAssign(n + 1), colAssign(m + 1) {
	}
	void addEdge(int u, int v) {
		adj[u].push_back(v);
	}
	int maximum_bipartite_matching() {
		int rt = 0;
		while (bfs()) {
			for (int i = 1; i <= n; i++)
				if (rowAssign[i] == NIL && dfs(i))
					rt++;
		}
		return rt;
	}
};
```