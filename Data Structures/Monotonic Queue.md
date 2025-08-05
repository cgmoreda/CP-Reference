```cpp
struct monotonicStack {  
    stack<pair<int, int>> stk;  
  
    void push(int val) {  
        stk.emplace(val, min(val, get_min()));  
    }  
  
    void pop() {  
        stk.pop();  
    }  
  
    int top() {  
        return stk.top().first;  
    }  
  
    int get_min() {  
        if (stk.empty())return INT_MAX;  
        return stk.top().second;  
    }  
      
    int size() {  
        return stk.size();  
    }  
  
    bool empty() {  
        return stk.empty();  
    }  
};  
  
struct monotonicQueue {  
    monotonicStack psh, pp;  
  
    void push(int val) {  
        psh.push(val);  
    }  
  
    void pop() {  
        move();  
        pp.pop();  
    }  
  
    int front() {  
        move();  
        return pp.top();  
    }  
  
    int get_min() {  
        return min(psh.get_min(), pp.get_min());  
    }  
  
    int size() {  
        return psh.size() + pp.size();  
    }  
  
    bool empty() {  
        return psh.empty() && pp.empty();  
    }  
  
    void move() {  
        if (pp.empty()) {  
            while (psh.size()) {  
                pp.push(psh.top());  
                psh.pop();  
            }  
        }  
  
    }  
};
```