void dfs2(int u, int par) {  
    if (reached[u])  
        return;  
    reached[u] = 1;  
    for (int i = 0; i < (int) g[u].size(); i++) {  
        edge &e = g[u][i];  
  
        if (par == e.to)continue;  
        if (e.flow == e.w) continue;  
        dfs2(e.to, u);  
    }  
}  
  
vector<ii > get_cut(int _s, int _t) {  
    max_flow(_s, _t);
    reached = vector<int>(n);  
    dfs2(s, -1);  
    vector<ii > ret;  
    for (int u = s; u <= t; u++) {  
        if (reached[u]) {  
            for (int i = 0; i < (int) g[u].size(); i++) {  
                edge &e = g[u][i];  
                if (!reached[e.to]) {  
                    ret.push_back({u, e.to});  
                }  
            }  
        }  
    }  
    return ret;  
}