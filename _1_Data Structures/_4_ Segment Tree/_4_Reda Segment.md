  
// Reda  Z
class segTree
{
 private:
	int leftmost, rightmost;
	segTree* lchild, * rchild;
	ll sum, lazy;
 public:
	segTree(int lf, int rt)
	{
		leftmost = lf;
		rightmost = rt;
		lazy = 0;
		if (leftmost == rightmost)
			sum = 0;
		else
		{
			int mid = (lf + rt) / 2;
			lchild = new segTree(lf, mid);
			rchild = new segTree(mid + 1, rt);
			calc();
		}
	}
	void prop()
	{
		if (lazy)
		{
			sum += (rightmost - leftmost + 1) * lazy;
			if (leftmost != rightmost)
				rchild->lazy += lazy, lchild->lazy += lazy;
			lazy = 0;
		}
	}
	void calc()
	{
		if (leftmost == rightmost)
			return;
		else
		{
			sum = lchild->sum + rchild->sum;
		}
	}
	void AddRange(int l, int r, ll val)
	{
		prop();
		if (rightmost < l || leftmost > r) return;
		if (l <= leftmost && r >= rightmost)
		{
			lazy += val, prop();
			return;
		}
		lchild->AddRange(l, r, val);
		rchild->AddRange(l, r, val);
		calc();
	}
	ll getRangeSum(int l, int r)
	{
		prop();
		if (l > rightmost || r < leftmost) return 0;
		if (l <= leftmost && r >= rightmost)
		{ return sum; }
		return lchild->getRangeSum(l, r) + rchild->getRangeSum(l, r);
	}
};