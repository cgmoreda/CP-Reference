```cpp
struct Node;
extern Node *emp;
struct Node {
  Node *left, *right;
  int val;
  Node() {
    left = right = this;
    val = 0;
  }
  Node(int val, Node *L = emp, Node *R = emp) : val(val), left(L), right(R) {}
};
Node *emp = new Node();
const int N = 2e5 + 5, MAX = 2e5 + 5;
Node *seg[N] = {emp};
Node *insert(Node *root, int start, int end, int idx) {
  if (idx > end || idx < start)
    return root;
  if (start == end) {
    return new Node(root->val + 1);
  }
  int mid = start + end >> 1;
  Node *L = insert(root->left, start, mid, idx);
  Node *R = insert(root->right, mid + 1, end, idx);
  return new Node(L->val + R->val, L, R);
}
int query(Node *L, Node *R, int start, int end, int k) {
  if (end <= k)
    return 0;
  if (start > k)
    return R->val - L->val;
  int mid = start + end >> 1;
  return query(L->left, R->left, start, mid, k) +
         query(L->right, R->right, mid + 1, end, k);
}
```