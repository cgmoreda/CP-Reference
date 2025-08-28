```cpp
const int N = 1e4 + 5;
int sz[N], head[N];
vector<int>heavy(N, -1);
vector<int>seq, idx(N);
vector<vector<pair<int, int>>>v(N);
int val[N];
int depth[N];
int n;
// segment tree here 
void dfsSz(int node, int par)
{
    int mx = 0;
    sz[node] = 1;
    for (auto it : v[node])
    {
        if (it.first == par)continue;
        dfsSz(it.first, node);
        val[it.first] = it.second;

        if (sz[it.first] > mx)mx = sz[it.first], heavy[node] = it.first;
        sz[node] += sz[it.first];
    }
}
int p[N];
void dfs(int node, int par, int h)
{
    p[node] = par;
    head[node] = h;
    idx[node] = seq.size();
    seq.push_back(node);
  
    depth[node] = depth[par] + 1;
    if (~heavy[node])
        dfs(heavy[node], node, h);
    for (auto it : v[node])
    {
        if (it.first == par || heavy[node] == it.first)continue;
        dfs(it.first, node, it.first);
    }
}
segment_tree<int> st(0);
int query(int a, int b) {
    int res = 0;
    for (; head[a] != head[b]; b = p[head[b]]) {
        if (depth[head[a]] > depth[head[b]])
            swap(a, b);
        int cur_heavy_path_max = st.query(idx[head[b]], idx[b]);
        res = max(res, cur_heavy_path_max);
    }
    if (depth[a] > depth[b])
        swap(a, b);
    if (a != b)
    {
        int last_heavy_path_max = st.query(idx[a] + 1, idx[b]);
        res = max(res, last_heavy_path_max);
    }
    return res;
}
void solve()
{
    seq.push_back(-1);
    cin >> n;
    vector<pair<int, int>>edges(n);
    heavy = vector<int>(n + 1, -1);
    for (int i = 1;i < n;i++)
    {
        int x, y, c;
        cin >> x >> y >> c;
        edges[i] = { x,y };
        v[x].push_back({ y,c });
        v[y].push_back({ x,c });
    }
    dfsSz(1, -1);
    dfs(1, N - 1, 1);
    st = segment_tree<int>(n+1);
    for (int i = 2;i <= n;i++)
        st.update(idx[i], idx[i], val[i]);
    while (true)
    {
        string q;
        cin >> q;
        if (q == "DONE")
        {
            seq.clear();
            for (int i = 1;i <= n;i++)
                v[i].clear();
            return;
        }
        if (q == "CHANGE")
        {
            int id, val;
            cin >> id >> val;
            int a = edges[id].first;
            int b = edges[id].second;
            if (p[a] == b)swap(a, b);
            st.update(idx[b], idx[b], val);
     
        }
        else
        {
            int a, b;
            cin >> a >> b;
            cout << query(a, b)<< endl;
        }
    }

}
```