  
// two segments
  
  
// To check if two segments intersect we will use the * signed area of the ABC triangle. This can be derived * from the cross product of the vectors AB and AC. 
 
bool intersect(Segment a, Segment b)  
{  
    Point p1 = { a.xi, a.yi }, p2 = { a.xf, a.yf }, p3 = { b.xi, b.yi }, p4 = { b.xf, b.yf };  
  
    return ((p4 - p1) ^ (p2 - p1)) * ((p2 - p1) ^ (p3 - p1)) >= 0 &&  
       ((p2 - p3) ^ (p4 - p3)) * ((p4 - p3) ^ (p1 - p3)) >= 0 &&  
       max(p1.x, p2.x) >= min(p3.x, p4.x) && max(p3.x, p4.x) >= min(p1.x, p2.x) &&  
       max(p1.y, p2.y) >= min(p3.y, p4.y) && max(p3.y, p4.y) >= min(p1.y, p2.y);  
}