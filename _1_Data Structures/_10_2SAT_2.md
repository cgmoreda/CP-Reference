```cpp
class two_sat
{
 public:
	two_sat(int n) : answer(n, -1), start(2 * n + 1)
	{
	}
	void add_or_clause(int x, bool valx, int y, bool valy)
	{
		x = x * 2 + valx;
		y = y * 2 + valy;
		edges.push_back({ x ^ 1, y });
		edges.push_back({ y ^ 1, x });
		++start[x ^ 1];
		++start[y ^ 1];
	}
	pair<bool, vector<int>> solve()
	{
		for (int i = 0; i + 1 < start.size(); ++i)
		{ start[i + 1] += start[i]; }
		proc();
		tos.resize(edges.size());
		for (const auto& p : edges)
		{ tos[start[p.first]++] = p.second; }
		proc();
		for (int i = 0; i < answer.size(); ++i)
		{
			if (answer[i] == -1)
			{
				lastv.clear();
				if (!dfs(2 * i))
				{
					for (int v : lastv)
					{ answer[v] = -1; }
					if (!dfs(2 * i + 1))
					{ return { false, {}}; }
				}
			}
		}
		return { true, answer };
	}
 private:
	void proc()
	{
		for (int i = start.size() - 1; i; --i)
		{ start[i] = start[i - 1]; }
		start[0] = 0;
	}
	bool dfs(int v)
	{
		lastv.push_back(v / 2);
		answer[v / 2] = v % 2;
		for (int i = start[v]; i < start[v + 1]; ++i)
		{
			const int to = tos[i];
			if ((answer[to / 2] != -1 && answer[to / 2] != to % 2) || (answer[to / 2] == -1 && !dfs(to)))
			{ return false; }
		}
		return true;
	}
	vector<int> answer, lastv, start, tos;
	vector<pair<int, int>> edges;
};
```