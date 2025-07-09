  
static const int N = 3e5 + 500;  
// if needed more than one thingy or complex merging  
struct W  
{  
    int sum, sum2;  
    int lz;  
    W operator+(W he) const  
    {  
       // up  
       return { (sum + he.sum) % mod, (sum2 + he.sum2) % mod, 0 };  
    }  
  
    void prop(int len)  
    {  
       // prop lazy  
       lz %= mod;  
       sum2 += lz * lz % mod * len + 2 * sum * lz;  
       sum += len * lz;  
       sum2 %= mod;  
       sum %= mod;  
       lz = 0;  
    }  
};  
W seg[4 * N], def = { 0 };  
int n, l, r, val;  
  
void dostuff(int p, int s, int e)  
{  
    // down  
    if (s != e)  
       seg[p * 2].lz += seg[p].lz, seg[p * 2 + 1].lz += seg[p].lz;  
    seg[p].prop(e - s + 1);  
}  
void update(int p = 1, int s = 1, int e = n)  
{  
    dostuff(p, s, e);  
    if (outofrange)return;  
    if (inrange)  
    {  
       seg[p].lz += val;  
       dostuff(p, s, e);  
       return;  
    }  
    update(lchild), update(rchild);  
    seg[p] = seg[p * 2] + seg[p * 2 + 1];  
}  
  
W get(int p = 1, int s = 1, int e = n)  
{  
    dostuff(p, s, e);  
    if (outofrange)  
       return def;  
    if (inrange)  
       return seg[p];  
    return get(lchild) + get(rchild);  
}