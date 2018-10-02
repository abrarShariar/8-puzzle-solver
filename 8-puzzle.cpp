#include<iostream>
#include <bits/stdc++.h>
using namespace std;
#define N 3

// node
struct Node {
  Node* parent;
  int board[N][N];
  int x, y;
  int cost;
  int level;
};

// Comparison struct to be used to order the heap
struct comp
{
    bool operator()(const Node* lhs, const Node* rhs) const
    {
        return (lhs->cost + lhs->level) > (rhs->cost + rhs->level);
    }
};

int printMatrix(int board[N][N]) {
  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      cout<<board[i][j]<<" ";
    }
    cout<<endl;
  }
}

// Function to allocate a new node
Node* newNode(int board[N][N], int x, int y, int newX,
              int newY, int level, Node* parent)
{
    Node* node = new Node;
    node->parent = parent;

    memcpy(node->board, board, sizeof node->board);
    swap(node->board[x][y], node->board[newX][newY]);

    node->cost = INT_MAX;
    node->level = level;

    node->x = newX;
    node->y = newY;

    return node;
}

// bottom, left, top, right
int row[] = { 1, 0, -1, 0 };
int col[] = { 0, -1, 0, 1 };

// Function to calculate the the number of misplaced tiles
int calculateCost(int initial[N][N], int final[N][N])
{
    int count = 0;
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++)
        if (initial[i][j] && initial[i][j] != final[i][j])
           count++;
    return count;
}

// Function to check if x,y is a valid matrix cordinate
int isSafe(int x, int y)
{
    return (x >= 0 && x < N && y >= 0 && y < N);
}

// print path from root node to dest node
void printPath(Node* root)
{
    if (root == NULL)
        return;
    printPath(root->parent);
    printMatrix(root->board);

    printf("\n");
}

void solve(int initial[N][N], int x, int y,
           int final[N][N])
{
    // Create a priority queue to store live nodes of
    priority_queue<Node*, std::vector<Node*>, comp> pq;

    // make root node and calculate its cost
    Node* root = newNode(initial, x, y, x, y, 0, NULL);
    root->cost = calculateCost(initial, final);

    pq.push(root);
    while (!pq.empty())
    {
        Node* min = pq.top();
        pq.pop();

        // if min is the goal
        if (min->cost == 0)
        {
            printPath(min);
            return;
        }

        for (int i = 0; i < 4; i++)
        {
            if (isSafe(min->x + row[i], min->y + col[i]))
            {
                Node* child = newNode(min->board, min->x,
                              min->y, min->x + row[i],
                              min->y + col[i],
                              min->level + 1, min);
                child->cost = calculateCost(child->board, final);

                pq.push(child);
            }
        }
    }
}

int main()
{
    int initial[N][N] =
    {
        {1, 2, 3},
        {5, 6, 0},
        {7, 8, 4}
    };

    int final[N][N] =
    {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 0}
    };

    // Blank tile coordinates
    int x = 1, y = 2;

    solve(initial, x, y, final);

    return 0;
}
