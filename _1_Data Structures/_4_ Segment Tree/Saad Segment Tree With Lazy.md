
template<typename T>
class segment_tree {//1-based
#define LEFT (idx<<1)
#define RIGHT (idx<<1|1)
#define MID ((start+end)>>1)
#define lchild LEFT, start, MID, from, to
#define rchild RIGHT, MID + 1, end, from, to
#define in from <= start && end <= to
#define out to < start || end < from
#define para int idx, int start, int end

    int n;
    vector<T> tree,lazy;
    
    T merge(const T &left, const T &right) {
    }
    
    inline void pushdown( para ) {
        if (lazy[idx] == 0)
            return;
        tree[idx] += lazy[idx];
        if (start != end) {
            lazy[LEFT] += lazy[idx];
            lazy[RIGHT] += lazy[idx];
        }
        lazy[idx] = 0;
    }

    inline void pushup(int idx) {
        tree[idx] = merge(tree[LEFT], tree[RIGHT]);
    }

    void build(para) {
        if (start == end)
            return;
        build(LEFT, start, MID);
        build(RIGHT, MID + 1, end);
        pushup(idx);
    }

    void build(para, const vector<T> &arr) {
        if (start == end) {
            tree[idx] = arr[start];
            return;
        }
        build(LEFT, start, MID, arr);
        build(RIGHT, MID + 1, end, arr);
        pushup(idx);
    }

    T query(para, int from, int to) {
        pushdown(idx, start, end);
        if (in)
            return tree[idx];
        if (to <= MID)
            return query(lchild);
        if (MID < from)
            return query(rchild);
        return merge(query(lchild),query(rchild));
    }

    void update(para, int from, int to,const T &val) {
        pushdown(idx, start, end);
        if (out)
            return;
        if (in) {
            lazy[idx] += val;
            pushdown(idx, start, end);
            return;
        }
        update(lchild,val);
        update(rchild, val);
        pushup(idx);
    }

public:
    segment_tree(int n) : n(n), tree(n << 2), lazy(n << 2) {
    }
    segment_tree(const vector<T> &v) {
        n = v.size() - 1;
        tree = lazy = vector<T>(n << 2);
        build(1, 1, n, v);
    }

    T query(int l, int r) {
        return query(1, 1, n, l, r);
    }

    void update(int l, int r, const T &val) {
        update(1, 1, n, l, r, val);
    }
};