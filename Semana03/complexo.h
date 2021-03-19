//
// Created by guilherme on 18/03/2021.
//


#ifndef COMPLEX_H
#define COMPLEX_H

#include <string>

#define POLAR 0x1
#define RET 0x2

class Complex{
    public:
        Complex();
        Complex(const double realPart, const double imaginaryPart, const int modo = RET );

        double getParteReal() const;
        double getParteImag() const;
        double abs() const;
        double arg() const;

        Complex* soma(const Complex* other) const;
        Complex* sub(const Complex* other) const;
        Complex* mult(const Complex* other) const;
        Complex* div(const Complex* other) const;

        std::string toString(const int modo) const;

    private:
        double real;
        double imaginaria;
};

#endif
