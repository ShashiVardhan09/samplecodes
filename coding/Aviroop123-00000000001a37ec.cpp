#include<bits/stdc++.h>
using namespace std;
#define pb push_back
// #define int long long
typedef long long ll;
#define fi first
#define se second
#define pii pair<int,int>
#define endl '\n'
#define fr(i, a, b) for(int i = a; i <= b; i++)
#define sz(s) (int)s.size()
#define y1 fdfbvfds
typedef long double f80;
#define all(x) x.begin(), x.end()

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
ll rand(ll l,ll r){
    uniform_int_distribution<ll> uid(l, r);
    return uid(rng);
}

const int N = 1e5 + 5;
int a[N];
int bit[N];

void upd(int idx,int val) {
    while(idx < N) {
        bit[idx] += val;
        idx += idx & (-idx);
    }
}

int sum(int idx) {
    int s = 0;
    while(idx > 0) {
        s += bit[idx];
        idx -= idx & (-idx);
    }
    return s;
}

int sum(int l,int r) {
    return sum(r) - sum(l - 1);
}

signed main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int T;
    cin >> T;
    fr(kase, 1, T) {
        cout << "Case #" << kase << ": ";
        int n;
        cin >> n;
        int pt = 0;
        fr(i, 1, n) {
            cin >> a[i];
            upd(a[i], 1);
            while(sum(pt + 1, N - 1) >= pt + 1) pt++;
            cout << pt;
            if(i < n)
                cout << " ";
        }
        fr(i, 1, n) {
            upd(a[i], -1);
        }
        cout << endl;
    }
    return 0;
}