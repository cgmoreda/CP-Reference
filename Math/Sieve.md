sieve--> get primes from 0 to N

const int N = 1e6 + 5;
vector <int> primes;
bool composite[N];
void sieve()
{
	composite[0] = composite[1] = 1;
	for (int i = 2; i < N; ++i)
	{
		if (composite[i])continue;
		primes.push_back(i);
		for (int j = 2; j < N; j += i)
			composite[j] = true;
	}
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

linear seive -->get primes from 0 to N 

const int N = 1e6;
vector <int> primes;
bool composite[N];
void sieve() 
{
	composite[0] = composite[1] = 1;
	for (int i = 2; i < N; ++i) 
	{
		if (!composite[i])primes.push_back(i);
		for (int j = 0; j < primes.size() && i * primes[j] < N; ++j)
		{
			composite[i * primes[j]] = 1;
			if (i % primes[j] == 0) break;
		}
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////

get prime factors using sieve (less than sqrt(n)) متنساش كود سبف قبلها

vector<int> prime_fact(int n)
{
	vector<int>temp;
	for (int i = 0;primes[i] * 1LL * primes[i] <= n;i++)
	{
		while (n % primes[i] == 0)
			temp.push_back(primes[i]), n /= primes[i];
	}
	if (n > 1)temp.push_back(n);
	return temp;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////

get divisors for all numbers from 1 to N

const int N = 1e5+5;
vector<vector<int>>divisors(N);
void generate_divisors() 
{
	for (int i = 1;i < N;i++)
	{
		for(int j=i;j<N;j+=i)
			divisors[j].push_back(i);
	}
}
/////////////////////////////////////////////////////////////////////////////////////////////////////

segmented_sieve --> get primes in range ex(1e9:1e9+1e6) o[(r-l)*loglog(r)+ o(sieve)]
 rمتنساش تستخدم سيف قبله لحد جذر ال
 const int N=1e5+5;
 bool composite[N];
void segmented_sieve()
{
	for(auto i:primes)
	{
		for(int j=max(i*i,(l+i-1)/i*i);j<=r;j+=i)
	     	composite[j-l]=1;                   // متسناش تنقص وانت بتسأل 
	}
	if(l==1)composite[0]=1;
}
