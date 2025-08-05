```cpp
class SparseSegtree {
private:
    struct Node {
        int freq = 0;
        bool lazy = 0;
        Node *left = nullptr;
        Node *right = nullptr;
    };
    Node *root = new Node;
    const int n;

    int comb(int a, int b) { return a + b; }

    void apply(Node *cur, int len, int val) {
        if(val == 1){
            (cur->lazy) ^= val;
            cur->freq = len - cur->freq;
        }
    }

    void push_down(Node *cur, int l, int r) {
        if ((cur->left) == nullptr) { (cur->left) = new Node; }
        if ((cur->right) == nullptr) { (cur->right) = new Node; }
        int m = (l + r) / 2;
        apply(cur->left, m - l + 1, cur->lazy);
        apply(cur->right, r - m, cur->lazy);
        cur->lazy = 0;
    }

    void flip_range(Node *cur, int l, int r, int ql, int qr, int val) {
        if (qr < l || ql > r) { return; }
        if (ql <= l && r <= qr) {
            apply(cur, r - l + 1, val);
        } else {
            push_down(cur, l, r);
            int m = (l + r) / 2;
            flip_range(cur->left, l, m, ql, qr, val);
            flip_range(cur->right, m + 1, r, ql, qr, val);
            (cur->freq) = comb((cur->left)->freq, (cur->right)->freq);
        }
    }

    int range_sum(Node *cur, int l, int r, int ql, int qr) {
        if (qr < l || ql > r) { return 0; }
        if (ql <= l && r <= qr) { return cur->freq; }
        push_down(cur, l, r);
        int m = (l + r) / 2;
        return comb(range_sum(cur->left, l, m, ql, qr),
                    range_sum(cur->right, m + 1, r, ql, qr));
    }

public:
    SparseSegtree(int n) : n(n) {}

    void flip_range(int ql, int qr, int val) { flip_range(root, 0, n - 1, ql, qr, val); }

    int range_sum(int ql, int qr) { return range_sum(root, 0, n - 1, ql, qr); }
};
```