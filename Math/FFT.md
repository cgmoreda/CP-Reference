```cpp
const double PI = acos(-1);
typedef complex<double> cd;
void fft(vector<cd>&a,bool invert){
    int n = a.size();
    if(n == 1)return;
    vector<cd>a0(n/2),a1(n/2);
    for(int i=0;i*2<n;i++){
        a0[i] = a[i*2];
        a1[i] = a[i*2+1];
    }
    fft(a0,invert);
    fft(a1,invert); // a(x) = a0(x^2) + x * a0(x^2)
    double angle = 2*PI/n * (invert ? -1 : 1);
    cd w = 1, wn(cos(angle),sin(angle));
    for(int i=0;i<n/2;i++){
        a[i] = a0[i] + w * a1[i];
        a[i + n/2] = a0[i] - w * a1[i];
        w*= wn;
        if(invert){
            a[i]/=2;
            a[i + n/2]/=2;
        }
    }
}
vector<ll> multiply(vector<ll>&a,vector<ll>&b){
    int n = 1;
    while(n < sz(a) + sz(b))n<<=1;
    vector<cd>fa(all(a)),fb(all(b));
    fa.resize(n);
    fb.resize(n);
    fft(fa,0);
    fft(fb,0);
    for(int i=0;i<n;i++){
        fa[i]*=fb[i];
    }
    fft(fa,1);
    vector<ll>res(n);
    for(int i=0;i<n;i++){
        res[i] = round(fa[i].real());
    }
    return res;
}
```