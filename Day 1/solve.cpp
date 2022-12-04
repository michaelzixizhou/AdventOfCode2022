#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main(){
    int most, second, third, curr = 0;
    string line;
    ifstream file("Day 1/day1input.txt");

    while (getline (file, line)) {
        if (line.empty()){
            curr = 0;
        } else {
            // cout << typeid(line).name() << endl;
            // cout << line << endl;

            curr += stoi( line );
        }
        if (curr > most){
            int temp = most; // saves first place
            most = curr; // curr -> first place
            curr = second; // set curr into first place
            second = temp; // first -> second
            third = curr;
        } else if (curr > second){
            int temp = second;
            second = curr;
            third = temp;
        } else if (curr > third) {
            third = curr;
        }

        // cout << most + second + third;
    }
    file.close();
    cout << most + second + third << endl;
    return 0;
}