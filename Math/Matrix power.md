struct matrix{
    int a[2][2];

    void init(){
        memset(a,0,sizeof(a));
        for(int i=0;i<2;i++)a[i][i]=1;
    }
    bool empty(){
        for(int i=0;i<2;i++)
            for(int j=0;j<2;j++)
                if(a[i][j]!=(i==j))return 1;
        return 0;
    }
    matrix(){
        memset(a,0,sizeof(a));
    }
    void debug()const{
#ifdef DEBUG
        cout<<"Start Matrix Debug:"<<endl;
        for(int i=1;i<2;i++){
            for(int j=1;j<2;j++)cout<<a[i][j]<<' ';
            cout<<endl;
        }
        cout<<"End Matrix Debug"<<endl;
#endif
    }
    matrix operator*(const matrix other)const{
        matrix result;
        for(int i=0;i<2;i++)
            for(int k=0;k<2;k++)
                for(int j=0;j<2;j++)
                    result.a[i][j]=(result.a[i][j]+(long long)a[i][k]*other.a[k][j])%mod;
        return result;
    }
    matrix operator+(const matrix other)const{
        matrix result;
        for(int i=0;i<2;i++)
            for(int j=0;j<2;j++)
                result.a[i][j]=(a[i][j]+other.a[i][j])%mod;
        return result;
    }
};

matrix fpow(matrix &x, ll n) {
    if (n == 0){
        matrix ret;
        ret.init();
        return ret;
    }
    if (n == 1)return x ;
    matrix ans = fpow(x, n / 2);
    ans = ans * ans;
    if (n & 1)ans = ans * x;
    return ans;
}

