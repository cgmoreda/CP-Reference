//TARJAN  
  
// preprocessor defines  
#define vi vector<int>  
#define vvi vector<vector<int>>  
#define vsi vector<set<int>>  
//SCC  
int n, m;  
vvi G;  
vi dn, dlow, onstack;  
stack<int> st;  
int id;  
void tarjan(int node)  
{  
    if (~dn[node])return;  
    ++id;  
    dn[node] = dlow[node] = id;  
    onstack[dn[node]] = 1;  
    st.push(node);  
    for (auto u : G[node])  
    {  
       if (dn[u] == -1)  
       {  
          tarjan(u);  
          dlow[node] = min(dlow[node], dlow[u]);  
       }  
       if (onstack[dn[u]])  
          dlow[node] = min(dlow[node], dlow[u]);  
    }  
    if (dlow[node] == dn[node])  
    {  
       int u = -1;  
       while (u != node)  
       {  
          u = st.top();  
          st.pop();  
          onstack[dn[u]] = 0;  
          dlow[u] = dlow[node];  
       }  
    }  
}  
void solve()  
{  
    cin >> n >> m;  
    st = stack<int>();  
    G = vvi(n + 1);  
    id = 0;  
    dn = vi(n + 2, -1);  
    onstack = dlow = vi(n + 2);  
  
// input graph  
    for (int i = 1; i < n; i++)if (dn[i] == -1)tarjan(i);  
// same dlow value means on same cycle  
}