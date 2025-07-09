const int N = 1e5 + 5,lvls = 18;
vector<vector<int>>v;
int n,timer,root,q,l,r,seq[2*N],dp[N][lvls+1];
vector<int>depth,start,endd,ans,freqNode;
int lca(int x, int y)
{
    if (depth[x] < depth[y])swap(x, y);
    for (int k = lvls;k >= 0;k--)
    {
        if (depth[x] - (1 << k) >= depth[y])x = dp[x][k];
    }
    if (x == y)return x;
    for (int k = lvls;k >= 0;k--)
        if (dp[x][k] != dp[y][k])x = dp[x][k], y = dp[y][k];
    return dp[x][0];
}
void dfs(int node, int par)
{
    start[node] = timer;
    seq[timer] = node;
    timer++;
    dp[node][0] = par;
    depth[node] = depth[par] + 1;
    for (auto it : v[node])
    {
        if (it == par)continue;
        dfs(it, node);
    }
    endd[node] = timer;
    seq[timer] = node;
    timer++;
}
void process()
{
    for (int k = 1;k <= lvls;k++)
    {
        for (int j = 0;j < n;j++)
        {
            if (dp[j][k - 1] == -1)continue;
            dp[j][k] = dp[dp[j][k - 1]][k - 1];
        }
    }
}
struct query
{
    int l, r, idx,lc;
    bool operator<(query& oth)const {
        if (l / root == oth.l / root)
            return r < oth.r;
        return l < oth.l;
    }
};
vector<query>ask;

void add(int idx)
{
    freqNode[seq[idx]]^=1;
    if (freqNode[seq[idx]] & 1);
    else ;
}
void remove(int idx)
{
    freqNode[seq[idx]]^=1;
    if (freqNode[seq[idx]] & 1);
    else;
}
void change(int idx)
{
    while (r < ask[idx].r)
    {
        r++;
        add(r);
    }
    while (l > ask[idx].l)
    {
        l--;
        add(l);
    }

    while (r > ask[idx].r)
    {
        remove(r);
        r--;
    }
    while (l < ask[idx].l)
    {
        remove(l);
        l++;
    }
    ans[ask[idx].idx];
    if(~ask[idx].lc);
}

void solve()
{
    timer = 0;
    l = 0, r = -1;
    cin>>n>>q;
    v=vector<vector<int>>(n);
    freqNode=start=endd=depth=vector<int>(n+5);
    ans=vector<int>(q);
    ask = vector<query>(q);
    root = sqrt(2*n) + 5;
    for (int i = 1;i < n;i++)
    {
        int x, y;
        cin >> x >> y;
        --x, --y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    dfs(0, n);
    process();
    for (int i = 0;i < q;i++)
    {
        int x, y;
        cin >> x >> y;
        --x, --y;
        int lc = lca(x, y);
        if (lc == x || lc == y)
        {
            ask[i].l = start[x];
            ask[i].r = start[y];
            ask[i].lc=-1;
        }
        else
        {
            if (start[x] > start[y])swap(x, y);
            ask[i].l = endd[x];
            ask[i].r = start[y];
            ask[i].lc=lc;
        }
        if (ask[i].l > ask[i].r)
            swap(ask[i].l, ask[i].r);
        ask[i].idx = i;
    }
    sort(all(ask));
    for (int i = 0;i < q;i++)change(i);
}

