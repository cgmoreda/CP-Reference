```cpp
int sqrtN;//use a constant value
struct query {
    int l, r, qindx, block;
    query() {}
    query(int l, int r, int qindx) : l(l), r(r), qindx(qindx), block(l / sqrtN) {}
    bool operator <(const query& q) {
        if (block != q.block)return block < q.block;
        return (block & 2 == 0 ? r<q.r : r>q.r);
    }

};
vector<query>q;
int curL, curR, ans;
void add(int indx);
void remove(int indx);
void solve(int l, int r) {
    while (curL > l)add(--curL);
    while (curR < r)add(++curR);
    while (curL < l)remove(curL++);
    while (curR > r)remove(curR--);
}
vector<int> MO() {
    vector<int>rt(q.size());
    ans = 0;
    curL = 1; curR = 0;
    add(0);
    sort(q.begin(), q.end());
    for (auto it : q) {
        solve(it.l, it.r);
        rt[it.qindx] = ans;
    }
    return rt;

}
```