#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main (int argc, char **argv) {
	if (argc >= 2) {
		string line;
		string output = "";
		ifstream input(argv[1]);
		if (input.is_open())
		{
			while (getline(input, line)) {
				int lineInt = std::stoi(line);
				string even;
				if (lineInt % 2 == 0) {
					even = " True";
				} else {
					even = " False";
				}
				output += line += even += '\n';
			}
			cout << output.substr(0, output.rfind('\n'));
			input.close();
		}
		else cout << "Unable to open file";
	}
	else cout << "Unable to open file";
	
	return 0;
}