class centroid_decomposition {  
    vector<bool> centroidMarked;  
    vector<int> size;  
  
    void dfsSize(int node, int par) {  
        size[node] = 1;  
        for (int ch: adj[node])  
            if (ch != par && !centroidMarked[ch]) {  
                dfsSize(ch, node);  
                size[node] += size[ch];  
            }  
    }  
  
    int getCenter(int node, int par, int size_of_tree) {  
        for (int ch: adj[node]) {  
            if (ch == par || centroidMarked[ch]) continue;  
            if (size[ch] * 2 > size_of_tree)  
                return getCenter(ch, node, size_of_tree);  
        }  
        return node;  
    }  
  
    int getCentroid(int src) {  
        dfsSize(src, -1);  
        int centroid = getCenter(src, -1, size[src]);  
        centroidMarked[centroid] = true;  
        return centroid;  
    }  
  
    int decomposeTree(int root) {  
        root = getCentroid(root);  
        solve(root);  
        for (int ch: adj[root]) {  
            if (centroidMarked[ch])  
                continue;  
            int centroid_of_subtree = decomposeTree(ch);  
//note: root and centroid_of_subtree probably not have a direct edge in adj  
            centroidTree[root].push_back(centroid_of_subtree);  
            centroidParent[centroid_of_subtree] = root;  
        }  
        return root;  
    }  
  
      
    void calc(int node, int par) {  
//TO-DO  
        for (int ch: adj[node])  
            if (ch != par && !centroidMarked[ch])  
                calc(ch, node);  
    }  
  
    void add(int node, int par) {  
//TO-DO  
        for (int ch: adj[node])  
            if (ch != par && !centroidMarked[ch])  
                add(ch, node);  
    }  
  
    void remove(int node, int par) {  
//TO-DO  
        for (int ch: adj[node])  
            if (ch != par && !centroidMarked[ch])  
                remove(ch, node);  
    }  
  
    void solve(int root) {  
//add root  
        for (int ch: adj[root])  
            if (!centroidMarked[ch]) {  
                calc(ch, root);  
                add(ch, root);  
            }  
//TO-DO //remove root  
        for (int ch: adj[root])  
            if (!centroidMarked[ch])  
                remove(ch, root);  
    }  
  
public:  
    int n, root;  
    vector<vector<int>> adj, centroidTree;  
    vector<int> centroidParent;  
  
    centroid_decomposition(vector<vector<int>> &adj) : adj(adj) {  
        n = (int) adj.size() - 1;  
        size = vector<int>(n + 1);  
        centroidTree = vector<vector<int>>(n + 1);  
        centroidParent = vector<int>(n + 1, -1);  
        centroidMarked = vector<bool>(n + 1);  
        root = decomposeTree(1);  
    }  
};