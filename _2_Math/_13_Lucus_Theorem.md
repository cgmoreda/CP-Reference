int N = 1e6 + 3, mod = 1e6 + 3;
// pre in O(mod),
struct combi
{
	int n;
	vector<int> facts, finvs, invs;
	combi(int _n) : n(_n), facts(_n), finvs(_n), invs(_n)
	{
		facts[0] = finvs[0] = 1;
		invs[1] = 1;
		for (int i = 2; i < n; i++)
		{
			invs[i] = 1LL * invs[mod % i] * (mod - mod / i) % mod;
		}
		for (int i = 1; i < n; i++)
		{
			facts[i] = 1LL * facts[i - 1] * i % mod;
			finvs[i] = 1LL * finvs[i - 1] * invs[i] % mod;
		}
	}
	inline int ncr(int x, int y)
	{
		if (y > x || y < 0) return 0;
		return 1LL * facts[x] * finvs[y] % mod * finvs[x - y] % mod;
	}
};
combi C(N);
// Computes nCr % mod using Lucas' Theorem when mod is a prime
int lucas(ll n, ll r)
{
	if (r > n) return 0;
	if (n < mod) return C.ncr(n, r);
	return 1LL * lucas(n / mod, r / mod) * lucas(n % mod, r % mod) % mod;
}