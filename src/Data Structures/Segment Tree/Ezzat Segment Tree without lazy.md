```cpp
template <typename T> class segment_tree { // 1-based
#define LEFT (idx << 1)
#define RIGHT (idx << 1 | 1)
#define MID ((start + end) >> 1)
  int n;
  vector<T> tree;
  T merge(const T &left, const T &right) { return left + right; }
  inline void pushup(int idx) { tree[idx] = merge(tree[LEFT], tree[RIGHT]); }
  T query(int idx, int start, int end, int from, int to) {
    if (start > to || end < from)
      return 0;
    if (start >= from && end <= to)
      return tree[idx];
    return merge(query(LEFT, start, MID, from, to),
                 query(RIGHT, MID + 1, end, from, to));
  }
  void update(int idx, int start, int end, int pos, const T &val) {
    if (pos < start || pos > end)
      return;
    if (start == end) {
      tree[idx] += val;
      return;
    }
    if (pos <= MID)
      update(LEFT, start, MID, pos, val);
    else
      update(RIGHT, MID + 1, end, pos, val);
    pushup(idx);
  }

public:
  segment_tree(int n) : n(n), tree(n << 2) {}

public:
  void update(int pos, const T &val) { update(1, 1, n, pos, val); }
  T query(int l, int r) { return query(1, 1, n, l, r); }

#undef LEFT
#undef RIGHT
#undef MID
};
```