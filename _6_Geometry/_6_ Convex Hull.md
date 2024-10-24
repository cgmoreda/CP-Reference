
void convexHull(vector<P> p, vector<P>& hull)  
{  
  
    sort(all(p), [&](P& a, P& b)  
    {  
      if (a.x != b.x)  
         return a.x < b.x;  
      return a.y < b.y;  
    });  
    if (p.size() == 1)  
    {  
       hull.push_back(p[0]);  
       return;  
    }  
    for (int rep = 0; rep < 2; rep++)  
    {  
       int s = hull.size();  
       for (int i = 0; i < p.size(); i++)  
       {  
          while (hull.size() >= s + 2)  
          {  
             P p1 = hull.end()[-2];  
             P p2 = hull.end()[-1];  
             if ((vec(p1, p2) ^ vec(p1, p[i])) < -eps)  
                break;  
  
             hull.pop_back();  
          }  
          hull.push_back(p[i]);  
       }  
       reverse(all(p));  
       hull.pop_back();  
    }  
}  