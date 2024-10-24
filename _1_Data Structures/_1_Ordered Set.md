#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
template<typename key>
using ordered_set = tree<key, null_type, less<key>, rb_tree_tag, tree_order_statistics_node_update>;

// order_of_key(k) : It returns to the number of items that are strictly smaller than our item k in O(logn) tme.
// find_by_order(k): It returns to an iterator to the kth element (counting from zero) in the set in O(logn) tme.
// To find the first element k must be zero.
