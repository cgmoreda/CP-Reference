```cpp
 class WaveletTree { // 0−based, values of arr better to be compressed
public:
  int low, high;
  WaveletTree ∗left, ∗right;
  vector<int> freq;

  WaveletTree(vector<int> &arr, int l, int r, int lo, int hi)
      : low(lo), high(hi), left(nullptr), right(nullptr) {
    if (lo == hi || l > r)
      return;
    int mid = (lo + hi) / 2;
    freq.reserve(r− l + 2);
    freq.push_back(0);
    for (int i = l; i <= r; i++) {
      freq.push_back(freq.back() + (arr[i] <= mid));
    }
    vector<int> leftArr, rightArr;
    for (int i = l; i <= r; i++) {
      if (arr[i] <= mid)
        leftArr.push_back(arr[i]);
      else
        rightArr.push_back(arr[i]);
    }
    if (!leftArr.empty()) {
      left = new WaveletTree(leftArr, 0, (int)leftArr.size()− 1, lo, mid);
    }
    if (!rightArr.empty()) {
      right =
          new WaveletTree(rightArr, 0, (int)rightArr.size()− 1, mid + 1, hi);
    }
  }

  int kth(int l, int r, int k) {
    if (low == high)
      return low;
    int inLeft = freq[r + 1]− freq[l];
    if (k <= inLeft) {
      return left− > kth(freq[l], freq[r + 1]− 1, k);
    } else {
      return right− > kth(l− freq[l], r− freq[r + 1], k− inLeft);
    }
  }

  int lte(int l, int r, int x) {
    if (x < low)
      return 0;
    if (x >= high)
      return r− l + 1;
    return (left ? left− > lte(freq[l], freq[r + 1]− 1, x) : 0) +
           (right ? right− > lte(l− freq[l], r− freq[r + 1], x) : 0);
  }

  int count(int l, int r, int x) {
    if (low == high)
      return (low == x) ? (r− l + 1) : 0;
    int mid = (low + high) / 2;
    if (x <= mid) {
      return left ? left− > count(freq[l], freq[r + 1]− 1, x) : 0;
    } else {
      return right ? right− > count(l− freq[l], r− freq[r + 1], x) : 0;
    }
  }
  ~WaveletTree() {
    delete left;
    delete right;
  }
};
```