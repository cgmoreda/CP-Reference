```cpp
struct segtree {  
    segtree *left = nullptr, *right = nullptr;  
    int mx = 0;  
  
    segtree(int val = 0) :  
            mx(val) {  
    }  
  
    void extend() {  
        if (left == nullptr) {  
            left = new segtree();  
            right = new segtree();  
        }  
    }  
  
    void pushup() {  
        mx = max(left->mx, right->mx);  
    }  
  
    ~segtree() {  
        if (left == nullptr)return;  
        delete left;  
        delete right;  
    }  
};  
  
class extened_segment_tree {  
#define MID ((start+end)>>1)  
  
    void update(segtree *root, int start, int end, int pos, int val) {  
        if (pos < start || end < pos)  
            return;  
        if (start == end) {  
            root->mx = max(root->mx, val);  
            return;  
        }  
        root->extend();  
        update(root->left, start, MID, pos, val);  
        update(root->right, MID + 1, end, pos, val);  
        root->pushup();  
    }  
  
    int query(segtree *root, int start, int end, int l, int r) {  
        if (root == nullptr || r < start || end < l)  
            return 0;  
        if (l <= start && end <= r)  
            return root->mx;  
        return max(query(root->left, start, MID, l, r),  
                   query(root->right, MID + 1, end, l, r));  
    }  
  
public:  
    int start, end;  
    segtree *root;  
  
    extened_segment_tree() {  
    }  
  
    ~extened_segment_tree() {  
        delete root;  
    }  
  
    extened_segment_tree(int start, int end) : start(start), end(end) {  
        root = new segtree();  
    }  
  
    void update(int pos, int val) {  
        update(root, start, end, pos, val);  
    }  
  
    int query(int l, int r) {  
        return query(root, start, end, l, r);  
    }  
  
#undef MID  
};
```