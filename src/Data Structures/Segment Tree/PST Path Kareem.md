```cpp
// values on nodes
struct Node {
    Node *left, *right;
    ll frq, sum;
    Node(ll frq, ll sum) : left(nullptr), right(nullptr), frq(frq), sum(sum) {}

    Node(Node *l, Node *r) : left(l), right(r), frq(l->frq + r->frq), sum(l->sum + r->sum) {}

};

struct PST {
private:
    int n;
    vector<Node *> roots;

    Node *build(int s, int e) {
        if (s == e) {
            return new Node(0ll, 0ll);
        }
        return new Node(build(s, (s + e) / 2), build((s + e) / 2 + 1, e));
    }

    Node *update(Node *prev, int s, int e, int idx, ll val) {
        if (s == e) {
            //cout<<"HI ";cout<<idx<<' '<<val<<' '<<(prev->frq)<<' '<<(prev->sum)<<endl;
            return new Node(1 + prev->frq, val + prev->sum);
        }
        int mid = (s + e) / 2;
        if (idx <= mid) {
            return new Node(update(prev->left, s, mid, idx, val), prev->right);
        } else {
            return new Node(prev->left, update(prev->right, mid + 1, e, idx, val));
        }
    }
    //kth element
    ll getKth(Node *u, Node *v, Node *lc, Node *upLc, int s, int e, ll k) {
        if (s == e)return s;
        int lVal = u->left->frq + v->left->frq - upLc->left->frq - lc->left->frq;
        if (lVal >= k) {
            return getKth(u->left, v->left, lc->left, upLc->left, s, (s + e) / 2, k);
        }
        return getKth(u->right, v->right, lc->right, upLc->right, (s + e) / 2 + 1, e, k - lVal);
    }

    pair<ll, ll> merge(const pair<ll, ll> &a, const pair<ll, ll> &b) {
        return {a.first + b.first, a.second + b.second};
    }
    // number of elements, sum of them in range
    pair<ll, ll> getRange(Node *u, Node *v, Node *lc, Node *upLc, int s, int e, int l, int r) {
        if (s > r || e < l)return {0, 0};
        if (s >= l && e <= r) {
            return {u->frq + v->frq - (upLc->frq) - lc->frq, u->sum + v->sum - (upLc->sum) - lc->sum};
        }
        return merge(getRange(u->left, v->left, lc->left, upLc->left, s, (s + e) / 2, l, r),
                     getRange(u->right, v->right, lc->right, upLc->right, (s + e) / 2 + 1, e, l, r));
    }

public:
    PST(int n) : n(n) {
        roots = vector<Node *>(n);
        roots[0] = build(0, n - 1);
    }

    void update(int u, int par, int idx, ll val) {
        roots[u] = update(roots[par], 0, n - 1, idx, val);
    }
    //kth element
    ll getKth(int u, int v, int lc, int upLC, ll k) {
        return getKth(roots[u], roots[v], roots[lc], roots[upLC], 0, n - 1, k);
    }
    // number of elements, sum of them in range
    pair<ll, ll> getRange(int u, int v, int lc, int upLc, int l, int r) {
        return getRange(roots[u], roots[v], roots[lc], roots[upLc], 0, n - 1, l, r);
    }
};
```