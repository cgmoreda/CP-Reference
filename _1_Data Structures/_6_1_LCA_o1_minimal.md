```cpp
  vector<int> dep(n), in(n), out(n), seq, pa(n, -1);

  auto dfs = [&](auto &&self, int u) -> void {
	in[u] = seq.size();
	seq.push_back(u);
	for (auto v : G[u])
	  if (v != pa[u]) {
		pa[v] = u, dep[v] = dep[u] + 1;
		self(self, v);
	  }
	out[u] = seq.size();
  };
  seq.reserve(n);
  dfs(dfs, 0);

  const int M = __lg(n);
  vector dp(M + 1, vector<int>(n));
  auto cmp = [&](int a, int b) { return dep[a] < dep[b] ? a : b; };

  dp[0] = seq;
  for (int i = 0; i < M; i++)
	for (int j = 0; j + (2 << i) <= n; j++)
	  dp[i + 1][j] = cmp(dp[i][j], dp[i][j + (1 << i)]);

  auto lca = [&](int a, int b) {
	if (a == b)return a;
	a = in[a] + 1, b = in[b] + 1;
	if (a > b)swap(a, b);
	int h = __lg(b - a);
	return pa[cmp(dp[h][a], dp[h][b - (1 << h)])];
  };
```