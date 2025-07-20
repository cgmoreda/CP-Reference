```cpp
long long getLaticeBoundryPoints(vector<P>& p)  
{  
    long long boundry = 0;  
    p.push_back(p[0]);  
    for (int i = 0; i < p.size() - 1; i++)  
    {  
       P a = vec(p[i], p[i + 1]);  
       boundry += __gcd(abs((int)a.x), abs((int)a.y));  
    }  
    p.pop_back();  
    return boundry;  
}  
long long getLaticeInsidePoints(vector<P>& p)  
{  
    return (getAreat2(p) - getLaticeBoundryPoints(p)) / 2 + 1;  
}  
```