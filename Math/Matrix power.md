```cpp
  
// const int M = 2;  
// typedef array<array<int, M>, M> matrix;

int mod = 1e9+7;
class matrix{
public:
    vector<vector<ll>>v;
    int n;
    matrix(int sz1){
        n = sz1;
        v = vector<vector<ll>>(n, vector<ll>(n));
    }
    matrix operator *(const matrix&a){
        matrix res(n);
        for(int i=0;i<n;i++){
            for(int k=0;k<n;k++){
                //if(v[i][k] == 0)continue;
                for(int j=0;j<n;j++){
                    res.v[i][j] +=  v[i][k] * a.v[k][j];
                    res.v[i][j]%=mod;
                }
            }
        }
        return res;
    }
    void ones(){
        for(int i=0;i<n;i++)v[i][i] = 1;
    }
};
matrix mpow(matrix a,ll k){
    matrix ans(a.n);
    ans.ones();
    while(k){
        if(k&1){
            ans = ans*a;
        }
        a = a*a;
        k>>=1;
    }
    return ans;
}
```