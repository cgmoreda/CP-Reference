```cpp
//There are n cities in Byteland but no roads between them. However, each day, a new road will be built. There will be a total of m roads.
//Your task is to process q queries of the form: "after how many days can we travel from city a to city b for the first time?"
int n, m, q;
struct query {
    int u,v;
};
vector<pair<int, int>> ed;
vector<int> low, high, ans;

void parallel_binary_search(vector<query> &qu) {
    while (true) {
        vector<vector<int>> adj(m);
        bool ok = 0;
        for (int i = 0; i < q; i++) {
            if (low[i] <= high[i]) {
                ok = 1;
                adj[(low[i] + high[i]) >> 1].push_back(i);
            }
        }
        if(!ok)break;
        DSU s(n + 1);
        auto valid = [&](int id)->bool{
            int l1 = s.Leader(qu[id].u);
            int l2 = s.Leader(qu[id].v);
            return l1 == l2;
        };
        for(int mid = 0; mid < m; mid++){
            s.Merge(ed[mid].first, ed[mid].second);
            for(auto&id : adj[mid]){
                if(valid(id)){
                    high[id] = mid - 1;
                    ans[id] = mid;
                }else low[id] = mid + 1;
            }
        }
    }
}

void solve() {
    cin >> n >> m>>q;
    ed = vector<pair<int, int>>(m);
    for (auto &[u, v]: ed){
        cin >> u >> v;
    }
    low = vector<int>(q, 0);
    high = vector<int>(q, m - 1);
    ans = vector<int>(q, -1);
    vector<query> qu(q);
    for (auto &[x, y]: qu)cin >> x >> y;
    parallel_binary_search(qu);
    for(int i =0;i<q;i++){
        if(qu[i].u == qu[i].v)cout<<0<<endl;
        else if(~ans[i])cout<<ans[i]+1<<endl;
        else cout<<-1<<endl;
    }
}
```