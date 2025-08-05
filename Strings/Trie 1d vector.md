```cpp
class Trie{
private:
    struct Node{
        map<char,int>mp;
        int leaf;
        bool have_next(char c){
            return mp.find(c)!=mp.end();
        }
        int& operator[](char c){
            return mp[c];
        }
        Node(){
            leaf = 0;
        }
    };
public:
    vector<Node>v;
    Trie(){
        v.push_back(Node());
    }
    void update(const string&s,int op){
        int cur = 0;
        for(auto&ch : s){
            if(!v[cur].have_next(ch)){
                v.push_back(Node());
                v[cur][ch] = v.size() - 1;
            }
            cur = v[cur][ch];
        }
        v[cur].leaf+=op;
    }
    int count(const string&s){
        int cur = 0;
        for(auto&it: s){
            if(!v[cur].have_next(it)){
                return 0;
            }
            cur = v[cur][it];
        }
        return v[cur].leaf;
    }
};

```