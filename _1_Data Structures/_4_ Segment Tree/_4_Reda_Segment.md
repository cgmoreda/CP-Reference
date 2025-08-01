// Reda Z
```cpp
struct segTree
{
	int lt, rt;
	segTree* lchild{}, * rchild{};
	ll sum{}, lazy{};

	static segTree pool[int(1e6)];
	static int top;

	static segTree* newNode()
	{
		return &pool[top++];
	}

	segTree(int lf = 0, int rt = 0) : lt(lf), rt(rt)
	{
	}

	static segTree* build(int _l, int _r)
	{
		auto node = newNode();
		node->lt = _l, node->rt = _r, node->lazy = 0;

		if (_l == _r)
		{
			node->sum = 0;
		}
		else
		{
			int mid = (_l + _r) / 2;
			node->lchild = build(_l, mid);
			node->rchild = build(mid + 1, _r);
			node->calc();
		}
		return node;
	}

	void prop()
	{
		if (lazy)
		{
			sum += (rt - lt + 1) * lazy;
			if (lt != rt)
			{
				lchild->lazy += lazy;
				rchild->lazy += lazy;
			}
			lazy = 0;
		}
	}

	bool calc()
	{
		return (lt != rt) and (sum = lchild->sum + rchild->sum);
	}

	void AddRange(int l, int r, ll val)
	{
		prop();
		if (rt < l || lt > r) return;
		if (l <= lt && r >= rt)
		{
			lazy += val;
			prop();
			return;
		}
		lchild->AddRange(l, r, val);
		rchild->AddRange(l, r, val);
		calc();
	}

	ll getRangeSum(int l, int r)
	{
		prop();
		if (l > rt || r < lt) return 0;
		if (l <= lt && r >= rt)
		{
			return sum;
		}
		return lchild->getRangeSum(l, r) + rchild->getRangeSum(l, r);
	}
	static void reset()
	{
		top = 0;
	}
};
segTree segTree::pool[int(1e6)];
int segTree::top = 0;
```