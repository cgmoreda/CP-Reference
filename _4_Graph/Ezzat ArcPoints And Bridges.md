  
void DAG()  
{  
  
    dag = vector<set<int>>(scc.size());  
  
    for (int i = 1; i < adj.size(); i++)  
  
       for (int j : adj[i])  
  
          if (compId[i] != compId[j])  
  
             dag[compId[i]].insert(compId[j]);  
  
}  
  
void DAG()  
{  
  
    dag = vector<set<int>>(scc.size());  
  
    for (int i = 1; i < adj.size(); i++)  
  
       for (int j : adj[i])  
  
          if (compId[i] != compId[j])  
  
             dag[compId[i]].insert(compId[j]);  
  
}  
  
  
  
// Articulation points and bridges  
  
vector<vector<int>> adj;  
  
vector<int> dfs_num, dfs_low;  
  
vector<bool> articulation_point;  
  
vector<pair<int, int>> bridge;  
  
stack<pair<int, int>> edges;  
  
vector<vector<pair<int, int>>> BCC; //biconnected components  
  
int timer, cntChild;  
  
void dfs(int node, int par)  
{  
  
    dfs_num[node] = dfs_low[node] = ++timer;  
  
    for (int child : adj[node])  
    {  
  
       if (par != child && dfs_num[child] < dfs_num[node])  
  
          edges.push({ node, child });  
  
       if (!dfs_num[child])  
       {  
  
          if (par == -1)  
  
             cntChild++;  
  
          dfs(child, node);  
  
          if (dfs_low[child] >= dfs_num[node])  
          {  
  
             articulation_point[node] = 1;  
  
//get biconnected component  
  
             BCC.push_back(vector<pair<int, int>>());  
  
             pair<int, int> edge;  
  
             do  
             {  
  
                edge = edges.top();  
  
                BCC.back().push_back(edge);  
  
                edges.pop();  
  
             } while (edge.first != node || edge.second != child);  
  
          }  
  
                            //can be (dfs_low[child] == dfs_num[child])  
  
          if (dfs_low[child] > dfs_num[node])   
  
          bridge.push_back({ node, child });  
  
          dfs_low[node] = min(dfs_low[node], dfs_low[child]);  
  
       }  
  
       else if (child != par)  
  
          dfs_low[node] = min(dfs_low[node], dfs_num[child]);  
  
    }  
  
}  
  
void articulation_points_and_bridges()  
{  
  
    timer = 0;  
  
    dfs_num = dfs_low = vector<int>(adj.size());  
  
    articulation_point = vector<bool>(adj.size());  
  
    bridge = vector<pair<int, int>>();  
  
    for (int i = 1; i < adj.size(); i++)  
  
       if (!dfs_num[i])  
       {  
  
          cntChild = 0;  
  
          dfs(i, -1);  
  
          articulation_point[i] = cntChild > 1;  
  
       }  
  
}