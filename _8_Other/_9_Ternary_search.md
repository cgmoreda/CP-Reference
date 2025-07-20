// 1 d ternary search

```cpp
bool can(int mid) {}
int ternary_search(int l, int r)
{
	int ans;
	while (l <= r)
	{
		int mid1 = l + (r - l) / 3;
		int mid2 = r - (r - l) / 3;
		if (can(mid1) > can(mid2))ans=mid1, r = mid2;
		else ans=mid2, l = mid1;
	}
	return ans;
}
```
// 2d, beware if dealing with double remove the +-1
```cpp
double get(int row,int mid);
double ans = 1e18;
double ternary1(int row)
{
    int l = -1e9 - 5, r = 1e9 + 5, mid1, mid2;
    double res;
    while (l <= r) {
        mid1 = l + (r - l) / 3;
        mid2 = r - (r - l) / 3;
        double res1 = get(row, mid1);
        double res2 = get(row, mid2);
        if (res1 > res2)
            l = mid1 + 1, res = res2;
        else
            r = mid2 - 1, res = res1;
    }
    return res;
}
void ternary2() 
{
    int l = -1e9 - 5, r = 1e9 + 5, mid1, mid2;
    while (l <= r) {
        mid1 = l + (r - l) / 3;
        mid2 = r - (r - l) / 3;
        double res1 = ternary1(mid1);
        double res2 = ternary1(mid2);
        if (res1 > res2)
        {
            ans = min(ans, res2);
            l = mid1 + 1;
        }
        else
        {
            ans = min(ans, res1);
            r = mid2 - 1;
        }
    }

}
```