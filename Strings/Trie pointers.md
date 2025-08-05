```cpp
class Trie{
private:

    struct Node{
        map<char,Node*>mp;
        int c;
        Node(){
            c = 0;
        }
    };
    Node*root;
    void destroy(Node*cur){
        for(auto&it :cur->mp){
            destroy(it.second);
        }
        delete cur;
    }
public:
    Trie(){
        root = new Node;
    }
    ~Trie(){
        destroy(root);
    }
    void update(const string&s,int op){
        Node*tmp = root;
        for(auto&it : s){
            if(tmp->mp.count(it) == 0){
                tmp->mp[it] = new Node;
            }
            tmp = tmp->mp[it];
            tmp->c+=op;
        }
    }
};

```