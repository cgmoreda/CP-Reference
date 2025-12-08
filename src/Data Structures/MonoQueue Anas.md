```cpp
template <class T>
struct Mono_queue {
    stack<pair<T, T>> pop_st, push_st;
 
    void push_to_stack(stack<pair<T, T>> &st, const T &val) {
        st.emplace(val, st.empty() ? val : max(val, st.top().second));
    }
 
    void push(const T &val) {
        push_to_stack(push_st, val);
    }
 
    void move() {
        if (!pop_st.empty()) return;
        while (!push_st.empty()) {
            push_to_stack(pop_st, push_st.top().first);
            push_st.pop();
        }
    }
 
    void pop(){
        move();
        pop_st.pop();
    }
 
    bool empty() const{
        return pop_st.empty() && push_st.empty();
    }
 
    int size() const{
        return pop_st.size() + push_st.size();
    }
 
    T get_max() const {
        if (pop_st.empty())
            return push_st.top().second;
        if (push_st.empty())
            return pop_st.top().second;
        return max(push_st.top().second, pop_st.top().second);
    }
};
```