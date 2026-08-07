```cpp
//undirected
vector<vector<int>>G;
vector<int>dfn,low;
int timer;
set<int>points;
void articulationPoint(int u, int p){
    dfn[u] = low[u] = ++timer;
    int childs = 0;
    for(auto&v : G[u]){
        if(v == p)continue;
        if(dfn[v] == -1){
            articulationPoint(v, u);
            low[u] = min(low[u],low[v]);
            if(dfn[u]<=low[v]&& ~p)points.insert(u);
            childs++;
        }else{
            low[u] = min(low[u],dfn[v]);
        }
    }
    if(childs >1 && p == -1)points.insert(u);
}
void init(int n){
    G = vector<vector<int>>(n + 1);
    dfn = low = vector<int>(n + 1,-1);
    points.clear();
    timer = 0;
}
```