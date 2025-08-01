```cpp
enum DIR
{
	L, R
};
 
template<typename T>
struct cartesian_tree
{
	static cartesian_tree<T>* sentinel;
	T key;
	int priority = 0, size = 0;
	bool reverse = false;
	cartesian_tree* child[2];
	cartesian_tree* parent;
	cartesian_tree()
	{
		key = T();
		priority = 0;
		child[L] = child[R] = parent = this;
	}
	cartesian_tree(const T& x, int y) :
		key(x), priority(y)
	{
		size = 1;
		child[L] = child[R] = sentinel;
		parent = sentinel;
	}
	void push_down()
	{
		if (!reverse)
			return;
		reverse = 0;
		child[L]->doReverse();
		child[R]->doReverse();
	}
	void doReverse()
	{
		reverse ^= 1;
		swap(child[L], child[R]);
	}
	void push_up()
	{
		if (child[L] != sentinel)child[L]->parent = this;
		if (child[R] != sentinel)child[R]->parent = this;
		size = child[L]->size + child[R]->size + 1;
	}
 
};
 
template<typename T>
cartesian_tree<T>* cartesian_tree<T>::sentinel = new cartesian_tree<T>();
 
template<typename T, template<typename> class cartesian_tree>
class implicit_treap
{ //1 based
	typedef cartesian_tree<T> node;
	typedef cartesian_tree<T>* nodeptr;
#define emptyNode cartesian_tree<T>::sentinel
	nodeptr root;
 
	void split(nodeptr root, nodeptr& l, nodeptr& r, int firstXElment)
	{
		if (root == emptyNode)
		{
			l = r = emptyNode;
			return;
		}
		root->push_down();
		if (firstXElment <= root->child[L]->size)
		{
			split(root->child[L], l, root->child[L], firstXElment);
			r = root;
		}
		else
		{
			split(root->child[R], root->child[R], r,
				firstXElment - root->child[L]->size - 1);
			l = root;
		}
		root->push_up();
	}
 
	nodeptr merge(nodeptr l, nodeptr r)
	{
		l->push_down();
		r->push_down();
		if (l == emptyNode || r == emptyNode)
			return (l == emptyNode ? r : l);
		if (l->priority > r->priority)
		{
			l->child[R] = merge(l->child[R], r);
			l->push_up();
			return l;
		}
		r->child[L] = merge(l, r->child[L]);
		r->push_up();
		return r;
	}
	vector<nodeptr> split_range(int s, int e)
	{ // [x<s,s<=x<=e,e<x]
		nodeptr l, m, r, tmp;
		split(root, l, tmp, s - 1);
		split(tmp, m, r, e - s + 1);
		return { l, m, r };
	}
	map<T, nodeptr> mp;
 public:
	implicit_treap() :
		root(emptyNode)
	{
	}
	int size()
	{
		return root->size;
	}
	void insert(int pos, const T& key)
	{
 
		nodeptr tmp = new node(key, rand());
		nodeptr l, r;
		split(root, l, r, pos - 1);
		root = merge(merge(l, tmp), r);
	}
	void push_back(const T& value)
	{
		nodeptr tmp = new node(value, rand());
		mp[value] = tmp;
		root = merge(root, tmp);
	}
	T getByIndex(int pos)
	{
 
		vector<nodeptr> tmp = split_range(pos, pos);
		nodeptr l = tmp[0], m = tmp[1], r = tmp[2];
		T rt = m->key;
		root = merge(merge(l, m), r);
		return rt;
	}
	void erase(int pos)
	{
		vector<nodeptr> tmp = split_range(pos, pos);
		nodeptr l = tmp[0], m = tmp[1], r = tmp[2];
		delete m;
		root = merge(l, r);
	}
	void cyclic_shift(int s, int e)
	{ //to the right
		vector<nodeptr> tmp = split_range(s, e);
		nodeptr l = tmp[0], m = tmp[1], r = tmp[2];
		nodeptr first, second;
		split(m, first, second, e - s);
		root = merge(merge(merge(l, second), first), r);
	}
	void reverse_range(int s, int e)
	{
		vector<nodeptr> tmp = split_range(s, e);
		nodeptr l = tmp[0], m = tmp[1], r = tmp[2];
		m->doReverse();
		root = merge(merge(l, m), r);
	}
	node range_query(int s, int e)
	{
		vector<nodeptr> tmp = split_range(s, e);
		nodeptr l = tmp[0], m = tmp[1], r = tmp[2];
		node rt = *m;
		root = merge(merge(l, m), r);
	}
	int getIndexByValue(const T& value)
	{
		nodeptr cur = mp[value];
 
		vector<nodeptr> path;
		path.push_back(cur);
		while (cur != root)
		{
			cur = cur->parent;
			path.push_back(cur);
		}
 
		for (int i = path.size() - 1; i >= 0; i--)
			path[i]->push_down();
		for (auto& it : path)
			it->push_up();
 
		cur = mp[value];
		int cnt = cur->child[L]->size + 1;
		while (cur != root)
		{
			nodeptr par = cur->parent;
			if (par->child[R] == cur)cnt += par->child[L]->size + 1;
			cur = par;
		}
		return cnt;
	}
};
implicit_treap<int, cartesian_tree> tr;
```