```cpp
  
string letters = "0123456789ABCDEF";  
  
int toInt(char c)  
{  
    return letters.find(c);  
}  
  
int FromAnyBasetoDecimal(string in, int base)  
{  
    int res = 0;  
    for (int i = 0; i < in.size(); ++i)  
        res *= base, res += toInt(in[i]);  
    return res;  
}  
  
string FromDecimaltoAnyBase(int number, int base)  
{  
    if (number == 0)  
        return "0";  
    string res = "";  
    for (; number; number /= base)  
        res = letters[number % base] + res;  
    return res;  
}  
  
string toNegativeBase(int n, int negBase)  
{  
    if (n == 0)  
        return "0";  
    string ans = "";  
    while (n != 0)  
    {  
        int rem = n % negBase;  
        n /= negBase;  
        if (rem < 0)  
        {  
            rem += (-negBase);  
            n += 1;  
        }  
        ans += to_string(rem);  
    }  
    reverse(all(ans));  
    return ans;  
}  
  
void print(int x)  
{  
    if (x <= 1)  
    {  
        cout << x;  
        return;    }  
    print(x >> 1);  
    cout << (x & 1);  
}
```