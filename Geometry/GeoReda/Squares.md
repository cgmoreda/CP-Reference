  
bool issqare(P a, P b, P c, P d)  
{  
    if (a == b || a == c || a == d || b == c || b == c || c == d)  
       return false;  
  
    vector<ld> ds = {  
       a.dis(b), a.dis(c), a.dis(d),  
       b.dis(c), b.dis(d), c.dis(d)  
    };  
    sort(all(ds));  
    return ds[0] > 0 &&  
       abs(ds[2] - ds[3]) < 1e-8 &&  
       abs(ds[0] - ds[1]) < 1e-8 &&  
       abs(ds[1] - ds[2]) < 1e-8 &&  
       abs(ds[4] - ds[5]) < 1e-8;  
  
}