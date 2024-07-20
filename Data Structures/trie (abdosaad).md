struct trie
{
    trie* nxt[26]{};
    bool endOfWord = false;
    void insert(const string& s)
    {
        trie* current = this;
        for (auto ch : s)
        {
            int i = ch - 'a';
            if (current->nxt[i] == nullptr) current->nxt[i] = new trie;
            current = current->nxt[i];
        }
        current->endOfWord = true;
    }
    bool search(const string& s)
    {
        trie* current = this;
        for (auto ch : s)
        {
            int i = ch - 'a';
            if (current->nxt[i]==nullptr)return false;
            current = current->nxt[i];
        }
        return current->endOfWord;
    }
};




struct trie
{
    trie* nxt[2]{};
    void insert(int val)
    {
        trie* current = this;
        for (int i=30;i>=0;i--)
        {
            bool bit = val >> i & 1;
            if (current->nxt[bit] == nullptr) current->nxt[bit] = new trie;
            current = current->nxt[bit];
        }
    }
    int search(int val)
    {
        int ans = 0;
        trie* current = this;
        for (int i = 30;i >= 0;i--)
        {
            bool bit = val >> i & 1;
            if (current->nxt[!bit] == nullptr)
                current = current->nxt[bit];
            else
                ans += (1 << i), current=current->nxt[!bit];
        }
        return ans;
    }
};

