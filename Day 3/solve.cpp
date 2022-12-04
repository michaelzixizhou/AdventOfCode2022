#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;


int priority(char a) {
    int c = a;
    // if (c >= 97) {
    //     return c - 96;
    // } else {
    //     return c - 38;
    // }

    return (c >= 97) ? c -96 : c - 38;
}

int solvept1(ifstream &a){
    string line;
    int total = 0;
    while (getline (a, line)) {
        string second_half = line.substr(line.length()/2, string::npos);
        for (int i = 0; i < line.length()/2; i++) {
            bool d = false;
            for (int j = 0; j < line.length()/2; j++) {
                if (line[i] == second_half[j]) {
                    total += priority(line[i]);
                    d = true;
                    break;
                }
            }
            if (d) break;
        }
    }
    cout << total << endl;
    return 0;
}


int main() {
    ifstream file("Day 3/day3input.txt");
    solvept1(file);
    file.close();
    return 0;
}