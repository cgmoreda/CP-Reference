```cpp
template <typename T>  
class FenwickTree2D {  
 public:  
  vector<vector<T>> tree;  
  int n, m;  
  void init(int n, int m) {  
    tree.assign(n + 2, vector<T>(m + 2, 0));  
    this->n = n;  
    this->m = m;  
  }  
  T merge(T &x, T &y) { return x + y; }  
  void update(int x, int y, T val) {  
    for (; x <= n; x += x & -x) {  
      for (int z = y; z <= m; z += z & -z) {  
        tree[x][z] = merge(tree[x][z], val);  
      }  
    }  
  }  
  T getPrefix(int x, int y) {  
    if (x <= 0) return 0;  
    T ret = 0;  
    for (; x; x -= x & -x) {  
      for (int z = y; z; z -= z & -z) {  
        ret = merge(ret, tree[x][z]);  
      }  
    }  
    return ret;  
  }  
  T getSquare(int xl, int yl, int xr, int yr) {  
    return getPrefix(xr, yr) + getPrefix(xl - 1, yl - 1) -  
           getPrefix(xr, yl - 1) - getPrefix(xl - 1, yr);  
  }  
};
```