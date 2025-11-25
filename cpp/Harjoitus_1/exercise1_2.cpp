#include <iostream>
#include <limits>
#include <iomanip>


int uChoice;
float uValue;
float priceWithVAT;
float VAT;

int main() {
    std::cout << "Anna veroton hinta:\n> ";
    while (!(std::cin >> uValue)){
        std::cout << "Väärä syöte. Anna luku:\n> ";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
    }
    std::cout << "Anna arvonlisäverokanta\n1) 0%\n2) 10%\n3) 14%\n4) 25.5%\n> ";
    std::cin >> uChoice;

    switch(uChoice) {
        case 1:
            priceWithVAT = uValue * 1.0;
            VAT = 0;
            break;
        case 2:
            priceWithVAT = uValue * 1.10;
            VAT = uValue * 0.10;
            break;
        case 3:
            priceWithVAT = uValue * 1.14;
            VAT = uValue * 0.14;
            break;
        case 4:
            priceWithVAT = uValue * 1.255;
            VAT = uValue * 0.255;
            break;
        default:
            std::cout << "Väärä tai virheellinen syöte" << "\n";
            main();
    }
    return 0; 
}