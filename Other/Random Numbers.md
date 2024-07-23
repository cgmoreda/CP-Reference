#include <chrono>  
#include <random>  
  
//write this line once in top  
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count() *  
               ((uint64_t) new char | 1));  
  
// use this instead of rand()  
template<typename T>  
T Rand(T low, T high) {  
    return uniform_int_distribution<T>(low, high)(rng);  
}