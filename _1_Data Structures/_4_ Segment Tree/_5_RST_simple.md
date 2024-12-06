
#define outofrange l > e || s > r
#define inrange l <= s && e <= r
#define lchild p * 2, s, (s+e)/2
#define rchild p * 2 + 1, (s+e)/2 + 1, e

static const int N = 3e5 + 500;
// if needed more than one thingy or complex merging
struct W
{
	int sum, mx, mn;
	W operator+(W he) const
	{
		return { sum + he.sum, max(mx, he.mx), min(mn, he.mn) };
	}
};
W seg[4 * N], def = { 0 }, val;
int n, l, r;

void update(int p = 1, int s = 1, int e = n)
{
	if (outofrange)return;
	if (inrange)
	{
		seg[p] = val;
		return;
	}
	update(lchild), update(rchild);
	seg[p] = seg[p * 2] + seg[p * 2 + 1];
}
W get(int p = 1, int s = 1, int e = n)
{
	if (outofrange)
		return def;
	if (inrange)
		return seg[p];
	return get(lchild) + get(rchild);
}
