```cpp
struct Node {
    Node *left, *right;
    ll val;

    Node(ll val) : left(nullptr), right(nullptr), val(val) {}

    Node(Node *l, Node *r) : left(l), right(r), val(l->val + r->val) {}
};

struct PST {
    int n;
    vector<Node*>roots;
    Node *build(int s, int e) {
        if (s == e) {
            return new Node(0);
        }
        return new Node(build(s, (s + e) / 2), build((s + e) / 2 + 1, e));
    }

    Node *update(Node *prev, int s, int e, int idx, ll val) {
        if (s == e) {
            return new Node(val);
        }
        int mid = (s + e) / 2;
        if (idx <= mid) {
            return new Node(update(prev->left, s, mid, idx, val), prev->right);
        } else {
            return new Node(prev->left, update(prev->right, mid + 1, e, idx, val));
        }
    }

    ll get(Node *cur, int s, int e, int l, int r) {
        if (s > r || e < l)return 0;
        if (s >= l && e <= r)return cur->val;
        return get(cur->left, s, (s + e) / 2, l, r) + get(cur->right, (s + e) / 2 + 1, e, l, r);
    }
    PST(int n) : n(n){
        roots.push_back(build(0,n-1));
    }
    void update(int k, int idx, ll x){
        roots[k] = update(roots[k], 0, n - 1, idx, x);
    }
    ll get(int k,int l,int r){
        return get(roots[k],0,n-1,l,r);
    }
    void makeCopy(int k){
        roots.push_back(roots[k]);
    }
};
```