```cpp
void genAllSubmask(int mask) {  
    for (int subMask = mask;; subMask = (subMask - 1) & mask) {  
//code  
        if (subMask == 0)  
            break;  
    }  
}
```