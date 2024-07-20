-#include <random>  
  
static std::random_device rd;  
static std::mt19937 gen(rd());  
  
int randomgen(int x)  
{  
    std::uniform_int_distribution<> dis(0, x - 1);  
    int rndnum = dis(gen);  
    return rndnum;  
}