#include<iostream>
#include <queue>          // std::priority_queue
using namespace std;

struct comp {
  bool operator()(const int& lhs, const int& rhs) const {
    // cout<<"lhs: "<<lhs<<endl;
    // cout<<"rhs: "<<rhs<<endl;
    return lhs < rhs;
  }
};


int main(){

  priority_queue<int, vector<int>, comp> pq;
  pq.push(10);
  pq.push(30);
  pq.push(20);
  pq.push(60);
  pq.push(40);
  pq.push(50);

  while(!pq.empty()){
    int el = pq.top();
    cout<<el<<endl;
    pq.pop();
  }


}
