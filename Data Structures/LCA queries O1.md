```cpp
const int N = 4e5 + 5, M = 20;
vector<vector<int>>adj;
int pw[N];
pair<int, int> dp[N][M + 1];
int lvl[N];
vector<pair<int, int>>et;
int indx[N];
void buildPower() {
    int indx = 1;
    for (int i = 1; i < N; i++) {
        if (i < (1 << indx))pw[i] = indx - 1;
        else {
            pw[i] = indx;
            indx++;
        }
    }
}
class LCA {
public:
    LCA() {
        et.clear();
        build();
    }
    
    void build() {
        dfs(1, -1);
        mem(indx, -1);
        
        for (int j = 0; j < et.size(); j++) {
            dp[j][0] = et[j];
            if (indx[et[j].second] == -1)indx[et[j].second] = j;
        }
        for (int i = 1; i <= M; i++) {
            for (int j = 0; j + (1 << i) - 1 < et.size(); j++) {
                dp[j][i] = min(dp[j][i - 1], dp[j + (1 << (i - 1))][i - 1]);
            }
        }

    }
    void dfs(int u, int par) {
        et.push_back({ lvl[u],u });
        for (auto i : adj[u]) {
            if (i != par) {
                lvl[i] = lvl[u] + 1;
                dfs(i, u);
                et.push_back({ lvl[u],u });
            }
        }
    }
    int lca(int u, int v) {
        int indxu = indx[u];
        int indxv = indx[v];
        if (indxu > indxv)swap(indxu, indxv);
        int indx = pw[indxv - indxu + 1];
        pair<int, int>ret = min(dp[indxu][indx], dp[indxv - (1 << indx) + 1][indx]);
        return ret.second;
    }
    int shortestPath(int u, int v) {
        return lvl[u] + lvl[v] - 2 * lvl[lca(u, v)];
    }
};
```