auto start = chrono::high_resolution_clock::now();  
// code    
auto stop = chrono::high_resolution_clock::now();  
    auto duration = chrono::duration_cast<chrono::nanoseconds>(stop - start);  
    cerr << "Time taken :"<< ((long double) duration.count()) / ((long double) 1e9) << " s" << endl;
    