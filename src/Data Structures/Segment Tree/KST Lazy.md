```cpp
class SegTreeLazy {
private:
#define outofrange s>r || e<l
#define inrange s>=l && e<=r
#define lchild p<<1, s, (s+e)/2
#define rchild p<<1|1, (s+e)/2+1, e

    struct Node {
        ll val, lz;

        Node(ll x = 0) {
            val = x;
            lz = 0;
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

    void prop(int p, int s, int e) {
        if (seg[p].lz) {
            seg[p].val += (e - s + 1) * seg[p].lz;
            if (s != e) {
                seg[p << 1].lz += seg[p].lz;
                seg[p << 1 | 1].lz += seg[p].lz;
            }
            seg[p].lz = 0;
        }
    }

    void update(int p, int s, int e, int l, int r, ll val) {
        prop(p, s, e);
        if (outofrange)return;
        if (inrange) {
            seg[p].lz += val;
            prop(p, s, e);
            return;
        }
        update(lchild, l, r, val);
        update(rchild, l, r, val);
        seg[p] = merge(seg[p << 1], seg[p << 1 | 1]);
    }

    ll def = {0};

    ll query(int p, int s, int e, int l, int r) {
        prop(p, s, e);
        if (outofrange)return def;
        if (inrange) {
            return seg[p].val;
        }
        return query(lchild, l, r) + query(rchild, l, r);
    }

    vector<Node> seg;
    int n;
public:
    SegTreeLazy(const vector<ll> &A) {
        int size = 1;
        while (size < sz(A))size <<= 1;
        n = sz(A);
        seg.resize(size << 1);
        build(1, 0, n - 1, A);
    }

    void update(int l, int r, ll val) {
        update(1, 0, n - 1, l, r, val);
    }

    ll query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }
};

```