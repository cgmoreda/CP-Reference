```cpp
//undirected
vector<int>adj[N];
int dfn[N],low[N];
set<int>points;
int cnt;
void articulationPoint(int node, int parent){
    dfn[node] = low[node] = ++cnt;
    int childs = 0;
    for(auto&ch : adj[node]){
        if(ch == parent)continue;
        if(dfn[ch] == -1){
            articulationPoint(ch, node);
            low[node] = min(low[node],low[ch]);
            if(dfn[node]<=low[ch]&& ~parent)points.insert(node);
            childs++;
        }else{
            low[node] = min(low[node],dfn[ch]);
        }
    }
    if(childs >1 && parent == -1)points.insert(node);
}
```