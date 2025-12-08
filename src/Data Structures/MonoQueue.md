```cpp
class MQ {
private:
    deque<pair<int, ll>> dq;
public:
    void push(int idx, ll x) {
        while (!dq.empty() && dq.back().second >= x) {
            dq.pop_back();
        }
        dq.push_back({idx, x});
    }

    ll get(int idx, int k) {
        while (!dq.empty() && idx - dq.front().first > k)dq.pop_front();
        if (dq.empty())return 1e9;
        return dq.front().second;
    }
};
```