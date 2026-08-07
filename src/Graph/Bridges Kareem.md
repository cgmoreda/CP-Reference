```cpp
//undirected
vector<vector<int>>G;
vector<int>dfn,low;
int timer;
void bridges(int u,int p){
    dfn[u] = low[u] = ++timer;
    for(auto&v : G[u]){
        if(v == p)continue;
        if(dfn[v] == -1){
            bridges(v,u);
            low[u] = min(low[u],low[v]);
            if(dfn[u] < low[v]){
                // is_bridge
            }
        }else{
            low[u] = min(low[u],dfn[v]);
        }
    }
}
void init(int n){
    G = vector<vector<int>>(n + 1);
    dfn = low = vector<int>(n + 1,-1);
    timer = 0;
}
```