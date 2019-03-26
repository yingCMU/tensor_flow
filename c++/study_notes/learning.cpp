// std refers to namespace std and the << operator passes sequences of characters to stdout. In fact, two sequences of characters get passed to stdout: "no more steering wheels" and std::endl, a newline character (std::endl also flushes the buffer).
#include <iostream>

int main() {
  std::cout << "no more steering wheels" << std::endl;
  return 0;
}


#include "Factorial.h"

int Factorial(int n) {
  int result = 1;

  for (int i = n; i > 0; --i) {
    result *= i;
  }

  return result;
}
