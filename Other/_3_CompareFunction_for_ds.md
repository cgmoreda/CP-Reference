```cpp
class comp {
    public:
       bool operator()(T a, T b){
           if(cond){
               return true;
           }
           return false;
      }
};

priority_queue<data_type, container, comparator> ds;
```