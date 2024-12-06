cpp
const int d=31;
int basis[d];
int sz;
bool insertVector(int mask) {
    for (ll i = d-1;i>=0; i--){
        if ((mask & 1<< i) == 0) continue;
        if (!basis[i]) {
            basis[i] = mask;
            sz++;
            return true;
        }
        mask ^= basis[i];
    }
    return false;
}
