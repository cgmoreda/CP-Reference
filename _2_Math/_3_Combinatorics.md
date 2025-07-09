  
/*  
* nCr = n!/((n-r)! * r!)  
* nCr(n,r) = nCr(n,n-r)  
* nPr = n!/(n-r)!  
* nPr(circle) = nPr/r  
* nCr(n,r) = pascal[n][r]  
* catalan[n] = nCr(2n,n)/(n+1)  
*/  
ull nCr(int n, int r) {  
    if (r > n)  
        return 0;  
    r = max(r, n - r);  
    ull ans = 1, div = 1, i = r + 1;  
    while (i <= n) {  
        ans *= i++;  
        ans /= div++;  
    }  
    return ans;  
}  
  
ull nPr(int n, int r) {  
    if (r > n)  
        return 0;  
    ull p = 1, i = n - r + 1;  
    while (i <= n)  
        p *= i++;  
    return p;  
}  
  
// return catalan number n-th using dp O(n^2)//max = 35 then overflow  
vector<ull> catalanNumber(int n) {  
    vector<ull> catalan(n + 1);  
    catalan[0] = catalan[1] = 1;  
    for (int i = 2; i <= n; i++) {  
        ull &rt = catalan[i];  
        for (int j = 0; j < n; j++)  
            rt += catalan[j] * catalan[n - j - 1];  
    }  
    return catalan;  
}  
  
// count number of paths in matrix n*m // go to right or down only  
ull countNumberOfPaths(int n, int m) {  
    return nCr(n + m - 2, n - 1);  
}