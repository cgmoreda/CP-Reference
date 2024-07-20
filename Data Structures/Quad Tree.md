//set NIL with defult value  
template<typename T>  
struct node {  
    node<T> *child[4];  
    T val;  
  
    node(T val = NIL) : val(val) {  
        memset(child, 0, sizeof child);  
    }  
  
    void push_up() {//merge the 4 childs  
        val = NIL;  
        for (int i = 0; i < 4; i++)  
            if (child[i] != nullptr) {}  
    }  
  
    ~node() {  
        for (int i = 0; i < 4; i++)  
            if (child[i] != nullptr)  
                delete child[i];  
    }  
};  
  
template<typename T>  
void update(node<T> *&root, int r1, int r2, int c1, int c2, int x, int y, T val) {  
    if (x < r1 || x > r2 || y < c1 || y > c2)  
        return;  
    if (root == nullptr)  
        root = new node<T>();  
    if (r1 == r2 && c1 == c2) {  
//update  
        return;  
    }  
    int rmid = (r1 + r2) / 2, cmid = (c1 + c2) / 2;  
    update(root->child[0], r1, rmid, c1, cmid, x, y, val);  
    update(root->child[1], r1, rmid, cmid + 1, c2, x, y, val);  
    update(root->child[2], rmid + 1, r2, c1, cmid, x, y, val);  
    update(root->child[3], rmid + 1, r2, cmid + 1, c2, x, y, val);  
    root->push_up();  
}  
  
template<typename T>  
T query(node<T> *root, int r1, int r2, int c1, int c2, int x, int y) {  
    if (root == nullptr || x < r1 || x > r2 || y < c1 || y > c2)  
        return NIL;  
    if (r1 == r2 && c1 == c2)  
        return root->val;  
    int rmid = (r1 + r2) / 2, cmid = (c1 + c2) / 2;  
    query(root->child[0], r1, rmid, c1, cmid, x, y);  
    query(root->child[1], r1, rmid, cmid + 1, c2, x, y);  
    query(root->child[2], rmid + 1, r2, c1, cmid, x, y);  
    query(root->child[3], rmid + 1, r2, cmid + 1, c2, x, y);  
}  
  
node<T> *seg = new node<T>();