```cpp
	auto start = chrono::high_resolution_clock::now();  
	// code    auto stop = chrono::high_resolution_clock::now();  
	auto duration = chrono::duration_cast<chrono::nanoseconds>(stop - start);  
	cerr << "Time taken :" << ((ld)duration.count()) / ((ld)1e9) << " s" << endl;
```