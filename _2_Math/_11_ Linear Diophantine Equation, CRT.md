ll exgcd(ll a,ll b, ll  &x, ll &y){
    if (a<0||b<0){
        ll g=exgcd(abs(a),abs(b),x,y);
        if (a<0)x*=-1;
        if (b<0)y*=-1;
        return g;
    }
    if (b == 0){
        x=1,y=0;
        return a;
    }
    ll g= exgcd(b,a%b,y,x);
    y-=(a/b)*x;
    return g;
}
ll ldioph(ll a,ll b, ll c,ll &x,ll &y, bool &found){
    ll g=exgcd(a,b,x,y);
    if (c%g){
        found=false;
        return g;
    }
    found=true;
    x*=c/g;
    y*=c/g;
    return g;
}
pair<ll,ll>CRT(const vector<ll>&a, const vector<ll>&m){
    ll rem=a[0],mod=m[0];
    int n=a.size();
    for (int i=1;i<n;i++){
        ll x,y;
        bool found=0;
        ll g= ldioph(mod,-m[i],a[i]-rem,x,y,found);

        if (!found)
            return {-1,-1};
        rem+=mod*x;
        mod=mod/g*m[i];
        rem=(rem%mod+mod)%mod;
    }
    return {rem,mod};

}