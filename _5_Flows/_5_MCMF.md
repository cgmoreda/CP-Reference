```cpp
  
struct MCMF //0-based  {  
    struct edge  
    {  
       int from, to, cost, cap, flow, backEdge;  
       edge()  
       {  
          from = to = cost = cap = flow = backEdge = 0;  
       }  
       edge(int from, int to, int cost, int cap, int flow, int backEdge) :  
          from(from), to(to), cost(cost), cap(cap), flow(flow),  
          backEdge(  
             backEdge)  
       {  
       }  
       bool operator<(const edge& other) const  
       {  
          return cost < other.cost;  
       }  
    };  
    int n, src, dest;  
    vector<vector<edge>> adj;  
  
    const int OO = 1e9;  
    MCMF(int n, int src, int dest) : n(n), src(src), dest(dest), adj(n)  
    {  
    }  
    void addEdge(int u, int v, int cost, int cap)  
    {  
       edge e1 = edge(u, v, cost, cap, 0, adj[v].size());  
       edge e2 = edge(v, u, -cost, 0, 0, adj[u].size());  
       adj[u].push_back(e1);  
       adj[v].push_back(e2);  
    }  
    pair<int, int> minCostMaxFlow()  
    {  
       int maxFlow = 0, cost = 0;  
       while (true)  
       {  
          vector<pair<int, int>> path = spfa();  
          if (path.empty())  
             break;  
          int new_flow = OO;  
          for (auto& it : path)  
          {  
             edge& e = adj[it.first][it.second];  
             new_flow = min(new_flow, e.cap - e.flow);  
          }  
          for (auto& it : path)  
          {  
             edge& e = adj[it.first][it.second];  
             e.flow += new_flow;  
             cost += new_flow * e.cost;  
             adj[e.to][e.backEdge].flow -= new_flow;  
          }  
          maxFlow += new_flow;  
       }  
       return { maxFlow, cost };  
    }  
    enum visit  
    {  
       finished, in_queue, not_visited  
    };  
    vector<pair<int, int>> spfa()  
    {  
       vector<int> dis(n, OO), prev(n, -1), from_edge(n), state(n,  
  
          not_visited);  
       deque<int> q;  
       dis[src] = 0;  
       q.push_back(src);  
       while (!q.empty())  
       {  
          int u = q.front();  
  
          q.pop_front();  
          state[u] = finished;  
          for (int i = 0; i < adj[u].size(); i++)  
          {  
             edge e = adj[u][i];  
             if (e.flow >= e.cap || dis[e.to] <= dis[u] + e.cost)  
                continue;  
             dis[e.to] = dis[u] + e.cost;  
             prev[e.to] = u;  
             from_edge[e.to] = i;  
             if (state[e.to] == in_queue)  
                continue;  
             if (state[e.to] == finished  
                || (!q.empty() && dis[q.front()] > dis[e.to]))  
                q.push_front(e.to);  
             else  
                q.push_back(e.to);  
             state[e.to] = in_queue;  
          }  
       }  
       if (dis[dest] == OO)  
          return {};  
       vector<pair<int, int>> path;  
       int cur = dest;  
       while (cur != src)  
       {  
          path.push_back({ prev[cur], from_edge[cur] });  
          cur = prev[cur];  
       }  
       reverse(path.begin(), path.end());  
       return path;  
    }  
};
```