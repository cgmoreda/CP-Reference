```cpp
  
vsi G;  
vi dn, dlow, pr;  
int id = 0, n;  
set<pair<int, int>> out;  
void bridges(int node)  
{  
    if (dn[node] != -1)  
       return;  
    dn[node] = dlow[node] = ++id;  
    for (auto u : G[node])  
    {  
       if (dn[u] == -1)  
       {  
          pr[u] = node;  
          bridges(u);  
          if (dn[node] < dlow[u])  
             out.insert({ min(node, u), max(node, u) });  
          dlow[node] = min(dlow[node], dlow[u]);  
       }  
       else if (u != pr[node])  
       {  
          dlow[node] = min(dlow[node], dn[u]);  
       }  
    }  
}  
void solve()  
{  
    out.clear();  
    dlow = vi(n + 1);  
    dn = pr = vi(n + 1, -1);  
    G = vsi(n + 1);  
// input graph  
    for (int i = 0; i < n; i++)if (dn[i] == -1)bridges(i);  
// out -> set with all bridges  
}
```