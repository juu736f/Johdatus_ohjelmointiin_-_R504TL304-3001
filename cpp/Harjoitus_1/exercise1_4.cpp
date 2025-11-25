#include <iostream>
#include <limits>
#include <iomanip>
#include <utility>

int min;
int hr;

int main() {
    std::cout << "Anna minuutit:\n> ";
    while (!(std::cin >> min)){
        std::cout << "Väärä syöte. Anna kokonaisluku:\n> ";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
    }
    if (min <= 0) {
        std::cout << "Minuutit eivät voi olla yhtä kuin tai vähemmän kuin 0\n";
        min = 0; 
        main();
    }
    hr = min / 60;
    min = min % 60;
    std::cout << "Tunnit: " << hr << "\nMinuutit: " << min << '\n';
}




