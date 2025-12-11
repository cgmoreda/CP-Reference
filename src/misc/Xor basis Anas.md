```cpp const int max_bit = 20;
struct xor_basis {
  array<int, max_bit> basis{};
  int cur_size = 0;

  bool insert(int mask) {
    for (int i = max_bit− 1; i >= 0;−−i) {
      if (((mask >> i) & 1) ^ 1)
        continue;
      if (!basis[i]) {

        basis[i] = mask;
        cur_size++;
        return 1;
      }
      mask ^= basis[i];
    }
    return 0;
  }

  bool can(int mask) {
    for (int i = max_bit− 1; i >= 0; i−−) {
      if (((mask >> i) & 1) ^ 1)
        continue;
      if (!basis[i])
        return 0;
      mask ^= basis[i];
    }
    return 1;
  }

  int get_kth_xor_subset(int k) {
    int tot = 1 << cur_size;
    if (k > tot)
      return−1;
    int ans = 0;
    for (int i = max_bit− 1; i >= 0; i−−) {
      if (!basis[i])
        continue;
      tot >>= 1;
      int on = (ans >> i) & 1;
      if ((k > tot) == on)
        ans ^= basis[i];
      if (k > tot)
        k− = tot;
    }
    return ans;
  }
};
```