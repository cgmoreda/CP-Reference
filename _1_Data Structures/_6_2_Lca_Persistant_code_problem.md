```cpp
#include<bits/stdc++.h> //Silence | ft. Reda , AbdoSa3d , Nourhan

using namespace std;

#define all(v) v.begin(),v.end()
#define ll long long
#define endl "\n"

struct Node
{
	Node* ls{}, * rs{};
	int sum{};
} pool[int(1e6)];
int top;
Node* null = pool + 0;
vector<Node*> rot;
void reset()
{
	top = 1;
	null->sum = 0;
	null->ls = null->rs = null;
}
Node* newNode()
{
	auto p = pool + (top++);
	*p = *null;
	return p;
}

// x is postion to insert
Node* add(Node* p, int l, int r, int x)
{
	auto np = newNode();
	*np = *p;
	np->sum++;
	if (r - l == 1)
	{
		return np;
	}
	int m = (l + r) / 2;
	if (x < m)
	{
		np->ls = add(p->ls, l, m, x);
	}
	else
	{
		np->rs = add(p->rs, m, r, x);
	}
	return np;
}

int R = 1e5 + 1;
int const N = 1e5 + 5, M = 20;
int dp[N][M + 1];
int lvl[N], n;
vector<vector<pair<int, int>>> G;

void dfs(int u, int par)
{
	dp[u][0] = par;
	for (auto [i, w] : G[u])
	{
		if (i != par)
		{
			lvl[i] = lvl[u] + 1;
			rot[i] = add(rot[u], 1, R, w);
			dfs(i, u);
		}
	}
}

int lca(int u, int v)
{
	if (lvl[u] > lvl[v])swap(u, v);
	for (int i = M; i >= 0; i--)
		if (lvl[v] - (1 << i) >= lvl[u])
			v = dp[v][i];

	if (u == v)return v;
	for (int i = M; i >= 0; i--)
	{
		int cu = dp[u][i], cv = dp[v][i];
		if (min(cu, cv) != -1 && cu != cv)
			u = cu, v = cv;
	}
	return dp[u][0];
}

void solve()
{
	reset();
	cin >> n;
	rot = vector<Node*>(n + 1);
	G = vector<vector<pair<int, int>>>(n + 1);
	rot[1] = null;
	for (int i = 1; i < n; i++)
	{
		int u, v, w;
		cin >> u >> v >> w;
		G[u].push_back({ v, w });
		G[v].push_back({ u, w });
	}
	dfs(1, -1);
	for (int i = 1; i <= M; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			int u = dp[j][i - 1];
			if (u == -1)dp[j][i] = -1;
			else dp[j][i] = dp[u][i - 1];
		}
	}
	auto get = [&](int a, int b, int c, int k)
	{
	  int l = 1, r = R;
	  Node* at = rot[a];
	  Node* bt = rot[b];
	  Node* pt = rot[c];
	  while (r - l > 1)
	  {
		  int sum = at->ls->sum + bt->ls->sum - 2 * pt->ls->sum;
		  if (sum >= k)
		  {
			  at = at->ls;
			  bt = bt->ls;
			  pt = pt->ls;
			  r = (r + l) / 2;
		  }
		  else
		  {
			  k -= sum;
			  at = at->rs;
			  bt = bt->rs;
			  pt = pt->rs;
			  l = (r + l) / 2;
		  }
	  }
	  return l;
	};

	int q;
	cin >> q;
	cout << fixed << setprecision(1);
	while (q--)
	{
		int a, b;
		cin >> a >> b;
		int c = lca(a, b);
		int cnt = lvl[a] + lvl[b] - 2 * lvl[c];
		if (cnt & 1)
		{
			int x = get(a, b, c, cnt / 2 + 1);
			cout << x * 1.0 << endl;
		}
		else
		{
			int x = get(a, b, c, cnt / 2);
			int y = get(a, b, c, cnt / 2 + 1);
			cout << (x + y) / 2.0 << endl;
		}

	}
}

int
main()
{
	cin.tie(0)->sync_with_stdio(0);

	int t = 1;
	cin >> t;
	while (t--)
		solve();

}
```