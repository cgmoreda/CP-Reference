```cpp
int n;
const int N = 1e5+5;
vector<int>v(N);
```
//عايز او يساوي شيل اليساوي 
```cpp
vector<int>next_mx()
{
	stack<int>st;
	st.push(n + 1);
	vector<int>suf;
	v[n + 1] = 2e9;
	for (int i = n;i > 0;i--)
	{
		while (v[i] >= v[st.top()])st.pop();
		suf.push_back(st.top());
		st.push(i);
	}
	suf.push_back(0);
	reverse(all(suf));
	return suf;
}
```

```cpp
vector<int>next_mn()
{
	stack<int>st;
	st.push(n + 1);
	vector<int>suf;
	v[n + 1] = -2e9;
	for (int i = n;i > 0;i--)
	{
		while (v[i] <= v[st.top()])st.pop();
		suf.push_back(st.top());
		st.push(i);
	}
	suf.push_back(0);
	reverse(all(suf));
	return suf;
}
```

```cpp
vector<int>prev_mx()
{
	vector<int>pre;
	stack<int>st;
	pre.push_back(0);
	st.push(0);
	v[0] = 2e9;
	for (int i = 1;i <= n;i++)
	{
		while (v[i] >= v[st.top()])st.pop();
		pre.push_back(st.top());
		st.push(i);
	}
	return pre;
}
```

```cpp
vector<int>prev_mn()
{
	vector<int>pre;
	stack<int>st;
	pre.push_back(0);
	st.push(0);
	v[0] = -2e9;
	for (int i = 1;i <= n;i++)
	{
		while (v[i] <= v[st.top()])st.pop();
		pre.push_back(st.top());
		st.push(i);
	}
	return pre;
}
```