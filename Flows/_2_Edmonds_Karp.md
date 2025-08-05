```cpp
//O( V * E * E)  
#define INF 0x3f3f3f3f3f3f3f3fLL  
int n;  
int capacity[101][101];  
  
int getPath(int src, int dest, vector<int> &parent) {  
    parent = vector<int>(n + 1, -1);  
    queue<pair<int, int>> q;  
    q.push({src, INF});  
    while (q.size()) {  
        int cur = q.front().first, flow = q.front().second;  
        q.pop();  
  
        if (cur == dest) return flow;  
        for (int i = 1; i <= n; i++)  
            if (parent[i] == -1 && capacity[cur][i]) {  
                parent[i] = cur;  
                q.push({i, min(flow, capacity[cur][i])});  
                if (i == dest) return q.back().second;  
            }  
    }  
    return 0;  
}  
int Edmonds_Karp(int source, int sink) {  
    int max_flow = 0;  
    int new_flow = 0;  
    vector<int> parent(n + 1, -1);  
    while (new_flow = getPath(source, sink, parent)) {  
        max_flow += new_flow;  
        int cur = sink;  
        while (cur != source) {  
            int prev = parent[cur];  
            capacity[prev][cur] -= new_flow;  
            capacity[cur][prev] += new_flow;  
            cur = prev;  
        };  
    }  
    return max_flow;  
}
```