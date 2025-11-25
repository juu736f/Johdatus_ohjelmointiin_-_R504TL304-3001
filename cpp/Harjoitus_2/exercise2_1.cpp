#include <iostream>
#include <string>
#include <limits>
#include <cmath>
const double pi = 3.141592653589793238462643383279;

int main() {
   int uChoice;
   while (true)
   {
      std::cout << "Valitse vaihtoehto\n1) Laske särmiön tilavuus\n2) Laske pallon tilavuus\n> ";
      if (std::cin >> uChoice) { break; }
      else {
         std::cout << "Väärä syöte. Anna kokonaisluku";
         std::cin.clear();
         std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
      }
   }

   if (uChoice == 1) {
      // V = a * b * c
      float a, b, c;
      while (true) {
         std::cout << "Anna särmiön korkeus:\n> ";
         if (std::cin >> a) { break; }
         else {
            std::cout << "Väärä syöte. Anna numero:\n>";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
         }
      }
      while (true) {
         std::cout << "Anna särmiön leveys:\n> ";
         if (std::cin >> b) { break; }
         else {
            std::cout << "Väärä syöte. Anna numero:\n>";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
         }
      }
      while (true) {
         std::cout << "Anna särmiön syvyys:\n> ";
         if (std::cin >> c) { break; }
         else {
            std::cout << "Väärä syöte. Anna numero:\n>";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
         }
      }
      double V = a * b * c;
      std::cout << "Tilavuus: " << V << '\n';
      return V;
   }
   if (uChoice == 2) {
      // V = 4/3 * π * r^3
      float r;
      while (true) {
         std::cout << "Anna pallon säde:\n> ";
         if (std::cin >> r) { break; }
         else {
            std::cout << "Väärä syöte. Anna numero:\n>";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
         }
      }
      double V = (4.0 / 3.0) * pi * std::pow(r,3);
      std::cout << "Tilavuus: " << V << '\n';
      return V;
   }
   else {
      std::cout << "Väärä syöte, valitse 1 tai 2";
      main();
   }
   return 0;
}
