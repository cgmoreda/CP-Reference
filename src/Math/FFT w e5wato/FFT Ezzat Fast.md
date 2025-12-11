```cpp

typedef valarray<complex<double>> polynomial;
const int LGN = 20;
vector<complex<double>> CM1[3][LGN + 1];
const double PI = acos(-1);
void prepare() {
    for (int sign = -1; sign <= 1; sign += 2) {
        for (int i = 0; i <= LGN; i++) {
            int N = 1 << i;
            double theta = sign * 2 * PI / N;
            complex<double> cm1 = 1;
            complex<double> cm2(cos(theta), sin(theta));
            for (int j = 0; j < N / 2; j++) {
                CM1[sign + 1][i].push_back(cm1);
                cm1 *= cm2;
            }
        }
    }
}
void fft(polynomial &a, int sign = -1) {
    int N = a.size();
    int lgn = log2(N);
    for (int m = N; m >= 2; m >>= 1, lgn--) {
        int mh = m >> 1;
        for (int i = 0; i < mh; i++) {
            const complex<double> &w = CM1[sign + 1][lgn][i];
            for (int j = i; j < N; j += m) {
                int k = j + mh;
                complex<double> x = a[j] - a[k];
                a[j] += a[k];
                a[k] = w * x;
            }
        }
    }
    int i = 0;
    for (int j = 1; j < N - 1; j++) {
        for (int k = N >> 1; k > (i ^= k); k >>= 1)
            ;
        if (j < i)
            swap(a[i], a[j]);
    }
}
valarray<ll> inv_fft(polynomial&& a) {
    complex<double> N = a.size();
    fft(a, 1);
    a /= N;
    valarray<ll> rt(a.size());
    for (int i = 0; i < a.size(); i++)
        rt[i] = round(a[i].real());
    return rt;
}
valarray<int> mul(const valarray<int> &a, const valarray<int> &b) {
	int adeg = (int) a.size() - 1, bdeg = (int) b.size() - 1;
	int N = 1;
	while (N <= adeg + bdeg)
		N <<= 1;
	polynomial A(N), B(N);
	for (int i = 0; i < a.size(); i++)
		A[i] = a[i];
	for (int i = 0; i < b.size(); i++)
		B[i] = b[i];
	fft(A);
	fft(B);
	polynomial m = A * B;
	inv_fft(m);
	return rt;
}
valarray<int> mul_with_mod(const vector<int> & a, const vector<int>& b, int MOD = 1e9 + 7) {
    int adeg = (int) a.size() - 1, bdeg = (int) b.size() - 1;
    int N = 1;
    while (N <= adeg + bdeg)
        N <<= 1;
    int C = sqrt(MOD);
    polynomial a1(N), a2(N);
    polynomial b1(N), b2(N);
    for (int i = 0; i < a.size(); ++i) {
        a1[i] = a[i] % C;
        a2[i] = a[i] / C;
    }
    for (int i = 0; i < b.size(); ++i) {
        b1[i] = b[i] % C;
        b2[i] = b[i] / C;
    }
    fft(a1), fft(a2);
    fft(b1), fft(b2);
    valarray<ll> m11 = inv_fft(a1 * b1) % MOD;
    valarray<ll> m12 = inv_fft(a1 * b2) % MOD;
    valarray<ll> m21 = inv_fft(a2 * b1) % MOD;
    valarray<ll> m22 = inv_fft(a2 * b2) % MOD;
    valarray<ll> res = m11 % MOD;
    res += C * (m12 + m21) % MOD;
    res += C * (C * m22 % MOD) % MOD;
    res %= MOD;
    valarray<int> rt(res.size());
    for (int i = 0; i < res.size(); i++)
        rt[i] = res[i];
    return rt;
}
```