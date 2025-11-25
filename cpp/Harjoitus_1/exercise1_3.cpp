#include <iostream>
#include <limits>
#include <iomanip>

float distance;
float economy = 6.5;

int main() {
    std::cout << "Anna matka:\n> ";
    while (!(std::cin >> distance)){
        std::cout << "Väärä syöte. Anna luku:\n> ";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
    }
    if (distance <= 0) {
        std::cout << "Matka ei voi olla yhtäkuin tai alle 0";
        distance = 0;
        main();
    }
    std::cout << "Polttoaineen kulutus on: " << economy * distance / 100 << " litraa\n\n";
    return 0;
}