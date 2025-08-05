```cpp
struct segtree
{
	static segtree* sentinel;
	segtree* left, * right;
	bool dirty = false;
	ll sum = 0, lazy = 0;

	segtree(ll val = 0) : sum(val)
	{
		left = right = this;
	}

	segtree(segtree* left, segtree* right) : left(left), right(right)
	{
		sum = left->sum + right->sum;
	}
};

segtree* segtree::sentinel = new segtree();

class persistent_segment_tree
{
#define MID ((start+end)>>1)

	segtree* apply(segtree* root, int start, int end, ll val)
	{
		segtree* rt = new segtree(*root);
		rt->dirty = true;
		rt->sum += (end - start + 1) * val;
		rt->lazy += val;
		return rt;
	}

	void pushdown(segtree* root, int start, int end)
	{
		if (root->dirty == false || start == end)
			return;
		root->left = apply(root->left, start, MID, root->lazy);
		root->right = apply(root->right, MID + 1, end, root->lazy);
		root->lazy = 0;
		root->dirty = 0;
	}

	segtree* build(int start, int end, const vector<int>& v)
	{
		if (start == end)
			return new segtree(v[start]);
		return new segtree(build(start, MID, v), build(MID + 1, end, v));
	}

	segtree* Set(segtree* root, int start, int end, int pos, ll new_val)
	{
		pushdown(root, start, end);
		if (pos < start || end < pos)
			return root;
		if (pos <= start && end <= pos)
			return new segtree(new_val);
		return new segtree(Set(root->left, start, MID, pos, new_val),
			Set(root->right, MID + 1, end, pos, new_val));
	}

	segtree* update(segtree* root, int start, int end, int l, int r, ll val)
	{
		pushdown(root, start, end);
		if (r < start || end < l)
			return root;
		if (l <= start && end <= r)
			return apply(root, start, end, val);
		return new segtree(update(root->left, start, MID, l, r, val),
			update(root->right, MID + 1, end, l, r, val));
	}

	ll query(segtree* root, int start, int end, int l, int r)
	{
		pushdown(root, start, end);
		if (r < start || end < l)
			return 0;
		if (l <= start && end <= r)
			return root->sum;
		return query(root->left, start, MID, l, r)
			+ query(root->right, MID + 1, end, l, r);
	}

 public:
	int start, end;
	vector<segtree*> versions;

	persistent_segment_tree(int start, int end) :
		start(start), end(end)
	{
		versions.push_back(segtree::sentinel);
	}

	persistent_segment_tree(const vector<int>& v) :
		start(0), end(v.size() - 1)
	{
		versions.push_back(build(start, end, v));
	}

	void update(int l, int r, ll val)
	{
		versions.push_back(update(versions.back(), start, end, l, r, val));
	}

	ll query(int time, int l, int r)
	{
		return query(versions[time], start, end, l, r);
	}

#undef MID
};
```