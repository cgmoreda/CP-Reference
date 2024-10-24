int const N = 1e5 + 5, M = 20;
int dp[N][M + 1];
int lvl[N], n;
int ans[N];
vector <vector<int>> adj;
 
void dfs(int u, int par) {
    dp[u][0] = par;
    for (auto i : adj[u]) {
        if (i != par) {
            lvl[i] = lvl[u] + 1;
            dfs(i, u);
        }
    }
}
 
void build() {
    //dfs(1, -1);
    for (int i = 1; i <= M; i++) {
        for (int j = 1; j <= n; j++) {
            int u = dp[j][i - 1];
            if (u == -1)dp[j][i] = -1;
            else dp[j][i] = dp[u][i - 1];
        }
    }
}
 
int lca(int u, int v) {
    if (lvl[u] > lvl[v])swap(u, v);
    for (int i = M; i >= 0; i--) {
        if (lvl[v] - (1 << i) >= lvl[u])
            v = dp[v][i];
    }
    if (u == v)return v;
    for (int i = M; i >= 0; i--) {
        int cu = dp[u][i], cv = dp[v][i];
        if (cu != -1 && cv != -1) {
            if (cu != cv)u = cu, v = cv;
        }
    }
    return dp[u][0];
}
 
int shortestPath(int u, int v) {
    return lvl[u] + lvl[v] - 2 * lvl[lca(u, v)];
}