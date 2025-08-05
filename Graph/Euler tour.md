```cpp  
void euler(vector<vector<int> >& adjMax, vector<int>& ret,  
    int n, int i, bool isDirected = false)  
{  
    for (int j = 0; j < n; j++)  
    {  
       if (adjMax[i][j])  
       {  
          adjMax[i][j]--;  
          if (!isDirected)  
             adjMax[j][i]--;  
          euler(adjMax, ret, n, j, isDirected);  
       }  
    }  
    ret.push_back(i);  
}
```