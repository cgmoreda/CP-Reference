  
//O(E*V)  
vector<vector<int>> adj;  
vector<int> rowAssign, colAssign, vis;//make vis array instance of vector  
int test_id;  
  
bool canMatch(int i) {  
    if (vis[i] == test_id) return false;  
    vis[i] = test_id;  
    for (int j: adj[i])  
        if (colAssign[j] == -1) {  
            colAssign[j] = i;  
            rowAssign[i] = j;  
            return true;  
        }  
    for (int j: adj[i])  
        if (canMatch(colAssign[j])) {  
            colAssign[j] = i;  
            rowAssign[i] = j;  
            return true;  
        }  
    return false;  
}  
// O(rows * edges) //number of operation could by strictly less than order (1e5*1e5->AC)  
int maximum_bipartite_matching(int rows, int cols) {  
    int maxFlow = 0;  
    rowAssign = vector<int>(rows, -1);  
    colAssign = vector<int>(cols, -1);  
    vis = vector<int>(rows);  
    for (int i = 0; i < rows; i++) {  
        test_id++;  
        if (canMatch(i)) maxFlow++;  
    }  
    vector<pair<int, int>> matches;  
    for (int j = 0; j < cols; j++)  
        if (~colAssign[j]) matches.push_back({colAssign[j], j});  
    return maxFlow;  
}