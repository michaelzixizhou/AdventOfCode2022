#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int matchup(char A, char B) {
    if (A == 'A') {
        if (B == 'X') {
            return 0 + 3;
        } else if (B == 'Y') {
            return 3 + 1;
        } else if (B == 'Z') {
            return 6 + 2;
        }
    } else if (A == 'B') {
        if (B == 'X') {
            return 0 + 1;
        } else if (B == 'Y') {
            return 3 + 2;
        } else if (B == 'Z') {
            return 6 + 3;
        }
    } else if (A == 'C') {
        if (B == 'X') {
            return 0 + 2;
        } else if (B == 'Y') {
            return 3 + 3;
        } else if (B == 'Z') {
            return 6 + 1;
        }
    }
    return 0;
}
 
int main() {
    string line;
    ifstream file("Day 2/day2input.txt");
    int total = 0;
    while (getline (file, line)) {
        total += matchup(line[0], line[2]);
    }
    file.close();
    cout << total << endl;
    return 0;
}