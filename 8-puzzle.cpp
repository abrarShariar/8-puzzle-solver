#include<iostream>
#include<queue>
using namespace std;
#define N 3

class Node {
  public:
    int board[N][N];
    int moves;
    int priority;
    Node* parent;

    Node() {};
    Node(int board[N][N], int moves, int priority, Node* parent) {
      this->board = board;
      this->moves = moves;
      this->priority = priority;
      this->parent = parent;
    };
};


int main() {

  vector<Node> priority_queue;
  int initialBoard[N][N] = {
    {8,1,3},
    {4,0,2},
    {7,6,5}
  };

  Node *parent;

  Node initialNode(initialBoard, 0, 0, parent);

}
