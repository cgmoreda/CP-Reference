```cpp
class SegTree {
private:
#define outofrange s>r || e<l
#define inrange s>=l && e<=r
#define lchild p<<1, s, (s+e)/2
#define rchild p<<1|1, (s+e)/2+1, e

    struct Node {
        ll val;

        Node(ll x = 0) {
            val = x;
        }

    };

    Node merge(const Node &a, const Node &b) {
        Node temp;
        temp.val = a.val + b.val;
        return temp;
    }

    void build(int p, int s, int e, const vector<ll> &A) {
        if (s == e) {
            seg[p].val = A[s];
            return;
        }
        build(lchild, A);
        build(rchild, A);
        seg[p] = merge(seg[p << 1], seg[p << 1 | 1]);
    }

    void update(int p, int s, int e, int idx, ll val) {
        if (s > idx || e < idx)return;
        if (s == e) {
            seg[p].val += val;
            return;
        }
        update(lchild, idx, val);
        update(rchild, idx, val);
        seg[p] = merge(seg[p << 1], seg[p << 1 | 1]);
    }

    ll def = {0};

    ll query(int p, int s, int e, int l, int r) {
        if (outofrange)return def;
        if (inrange) {
            return seg[p].val;
        }
        return query(lchild, l, r) + query(rchild, l, r);
    }

    vector<Node> seg;
    int n;
public:
    SegTree(const vector<ll> &A) {
        int size = 1;
        while (size < sz(A))size <<= 1;
        n = sz(A);
        seg.resize(size << 1);
        build(1, 0, n - 1, A);
    }

    void update(int idx, ll val) {
        update(1, 0, n - 1, idx, val);
    }

    ll query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }
};

```