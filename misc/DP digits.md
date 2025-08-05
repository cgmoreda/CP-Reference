```cpp
int n;
vector<int>v1, v2;
ll dp[20][2][2];
ll fun(int idx, bool l,bool r)
{

	if (idx == n)return 1;
	ll& ret = dp[idx][l][r];
	if (~ret)return ret;
	ret = 0;
	int lim1 = l? 0 : v1[idx];
	int lim2 = r? 9 : v2[idx];

	for (int i = lim1;i <=lim2;i++)
	{
		bool temp1 = i > v1[idx];
		bool temp2 = i < v2[idx];
	    ret += fun(idx + 1, l|temp1, r|temp2);
	}
	return ret;
}
void solve()
{
	memset(dp, -1, sizeof dp);
	ll x, y;
	cin >> x >> y;
	while (x)v1.push_back(x % 10), x /= 10;
	while (y)v2.push_back(y % 10), y /= 10;
	while (v1.size() < v2.size())v1.push_back(0);
	while (v2.size() < v1.size())v2.push_back(0);
	reverse(all(v1));
	reverse(all(v2));
	n = v1.size();
	cout << fun(0, 0, 0, 0) << endl;
	v1.clear();
	v2.clear();
}
```