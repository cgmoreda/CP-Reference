  
#define vi vector<int>  
#define vvi vector<vector<int>>  
#define vsi vector<set<int>>  
//SCC  
vvi G;  
vi dnum, dlow, pr;  
set<int> arc_point;  
  
int dfsroot, cntroot, id, n;  
void articulation_points(int node)  
{  
    if (dnum[node] != -1) return;  
    dnum[node] = dlow[node] = ++id;  
    for (auto u : G[node])  
    {  
       if (dnum[u] == -1)  
       {  
          pr[u] = node;  
          articulation_points(u);  
          if (dnum[node] <= dlow[u])  
             if (node == dfsroot)  
                cntroot++;  
             else  
                arc_point.insert(node);  
          dlow[node] = min(dlow[node], dlow[u]);  
       }  
       else if (u != pr[node])  
       {  
          dlow[node] = min(dlow[node], dnum[u]);  
       }  
    }  
}  
void solve()  
{  
    dlow = pr = vi(n + 1);  
    dnum = vi(n + 1, -1);  
    id = 0;  
    arc_point.clear();  
    G = vvi(n + 1);  
// input graph  
    for (int i = 0; i < n; i++)  
    {  
       dfsroot = i;  
       cntroot = 0;  
       articulation_points(i);  
       if (cntroot > 1)  
          arc_point.insert(i);  
    }  
}