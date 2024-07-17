  
string s, p;  
int f[(int)(1e6+100)];  
  
void search()  
{  
    int len = 0;  
    for (int i = 0; i < s.size(); ++i)  
    {  
       while (len > 0 && s[i] != p[len])  
          len = f[len - 1];  
       if (s[i] == p[len])  
          ++len;  
       if (len == p.size())  
       {  
          //cerr << i - len + 1 << endl;  
          len = f[len - 1];  
       }  
    }  
}  
void build()  
{  
    int len = 0;  
    f[0] = 0;  
    for (int i = 1; i < p.size(); ++i)  
    {  
       while (len > 0 && p[i] != p[len])  
          len = f[len - 1];  
       if (p[i] == p[len])  
          ++len;  
       f[i] = len;  
    }  
}