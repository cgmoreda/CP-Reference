```cpp
const int LG = 20;
const int N = 1e6 + 10;
int up[N][LG],lvl[N];
vector<vector<int>>G;
class LCA{
public:
    LCA(){
        dfs(1,0);
    }
    void dfs(int u,int p){
        up[u][0] = p;
        for(int j = 1;j<LG;j++){
            up[u][j] = up[up[u][j-1]][j-1];
        }
        for(auto&v : G[u]){
            if(v == p)continue;
            lvl[v] = lvl[u] + 1;
            dfs(v,u);
        }
    }
    int kthAncestor(int u,int k){
        for(int j = LG-1;j>=0;j--){
            if(k >> j &1){
                u = up[u][j];
            }
        }
        return u;
    }
    int lca(int u,int v){
        if(lvl[u] < lvl[v])swap(u,v);
        int d = lvl[u] - lvl[v];
        u = kthAncestor(u,d);
        if(u == v)return u;
        for(int j = LG-1;j>=0;j--){
            if(up[u][j] !=up[v][j]){
                u = up[u][j];
                v = up[v][j];
            }
        }
        return up[u][0];
    }
    int dist(int u,int v){
        return lvl[u] + lvl[v] - 2*lvl[lca(u,v)];
    }
};
```