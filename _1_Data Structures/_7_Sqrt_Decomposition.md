int root = (int)sqrt(n + .0) + 1;
vector<int> v(n), bucket(root);
for (int i = 0; i < n; ++i)
    bucket[i / root] += v[i];

while (q--) {
    int l, r;
    int sum = 0;
    int c_l = l / root, c_r = r / root;
    if (c_l == c_r)
        for (int i = l; i <= r; ++i)
            sum += v[i];
    else {
        for (int i = l, end = (c_l + 1) * root - 1; i <= end; ++i)
            sum += v[i];
        for (int i = c_l + 1; i <= c_r - 1; ++i)
            sum += bucket[i];
        for (int i = c_r * root; i <= r; ++i)
            sum += v[i];
    }
}