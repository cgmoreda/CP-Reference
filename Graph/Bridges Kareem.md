```cpp
//undirected
vector<int>adj[N];
int dfn[N],low[N],timer;
void bridges(int node,int parent){
    dfn[node] = low[node] = ++timer;
    for(auto&ch : adj[node]){
        if(ch == parent)continue;
        if(dfn[ch] == -1){
            bridges(ch,node);
            low[node] = min(low[node],low[ch]);
            if(dfn[node] < low[ch]){
                // is_bridge
            }
        }else{
            low[node] = min(low[node],dfn[ch]);
        }
    }
}
```