// get max  
ll l = 0, r = n;  
while (r - l >= 3) {  
    ll g = l + (r - l) / 3;  
    ll h = l + 2 * (r - l) / 3;  
    if (f(g) > f(h))  
        r = h;  
    else l = g;  
}  
ll ans = 0;  
for (ll i = l; i <= r; i++) {  
    ans = max(ans, f(i));  
}



