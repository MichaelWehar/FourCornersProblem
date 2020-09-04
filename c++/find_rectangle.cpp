// Code written by Niteesh Kumar & Michael Wehar
// Compiles with C++11

#include <bits/stdc++.h>
using namespace std;

bool searchForRectangle(int rows, int cols, bool** mat){
    // Make sure that matrix is non-trivial
    if (rows < 2 || cols < 2) {
        return false;
    }

    // Create map
    int num_of_keys;
    map<int, vector<int>> adjsList;
    if (rows >= cols) {
        cout << "row-wise" << endl;
        num_of_keys = rows;
        // Convert each row into vector of col indexes
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (mat[i][j]) {
                    adjsList[i].push_back(j);
                }
            }
        }
    } else {
        cout << "col-wise" << endl;
        num_of_keys = cols;
        // Convert each col into vector of row indexes
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (mat[i][j]) {
                    adjsList[j].push_back(i);
                }
            }
        }
    }

    // Search for a rectangle whose four corners are 1's
    map<pair<int, int>, int> pairs;
    for (int i = 0; i < num_of_keys; i++) {
        vector<int> values = adjsList[i];
        int size = values.size();
        for (int j = 0; j < size - 1; j++) {
            for (int k = j + 1; k < size; k++) {
                pair<int, int> temp = make_pair(values[j], values[k]);
                if (pairs.find(temp) != pairs.end()) {
                    // Prints rows followed by cols if row-wise
                    // Prints cols followed by rows if col-wise
                    cout << pairs[temp] << "," << i << endl;
                    cout << values[j] << "," << values[k] << endl;
                    return true;
                } else {
                    pairs[temp] = i;
                }
            }
        }
    }
    return false;
}

// Simple test case
int main(){
    // Dimensions
    int rows = 3;
    int cols = 4;
    // Matrix
    bool** mat = new bool*[rows];
    mat[0] = new bool[cols] { 0, 0, 1, 1 };
    mat[1] = new bool[cols] { 0, 0, 1, 0 };
    mat[2] = new bool[cols] { 1, 0, 1, 1 };
    // Search for a rectangle whose four corners are 1's
    if (searchForRectangle(rows, cols, mat)) {
        cout << "Exists" << endl;
    } else {
        cout << "Doesn't exist" << endl;
    }
    // Clean up and return
    delete[] mat[0];
    delete[] mat[1];
    delete[] mat[2];
    delete[] mat;
    return 0;
}
