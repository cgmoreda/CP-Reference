```cpp
string misereNim(const vector<int>& heaps) {
    int ones = 0;
    int moreThanOne = 0;
    int nimSum = 0;
 
    for (int h : heaps) {
        if (h == 1) ones++;
        else moreThanOne++;
        nimSum ^= h;
    }
 
    if (moreThanOne == 0) {
        // All heaps are 1
        return (ones % 2 == 0 ? "Win" : "Lose");
    } else if (moreThanOne == 1) {
        // One heap > 1
        return (ones % 2 == 1 ? "Win" : "Lose");
    } else {
        // General case
        return (nimSum == 0 ? "Lose" : "Win");
    }

```