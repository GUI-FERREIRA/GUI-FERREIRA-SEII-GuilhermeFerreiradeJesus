//
// Created by guilherme on 18/03/2021.
//
#include <sstream>
#include <math.h>
#include "complexo.h"


Complex::Complex()
{
    Complex::real = 0.0;
    Complex::imaginaria = 0.0;
}

Complex::Complex(const double realPart, const double imaginaryPart, const int modo)
{
    Complex::real = realPart;
    Complex::imaginaria = imaginaryPart;
    if (modo == POLAR){
        Complex::real = realPart * cos(imaginaryPart);
        Complex::imaginaria = realPart * sin(imaginaryPart);
    }
}

double Complex::getParteReal() const {
    return real;
}

double Complex::getParteImag() const {
    return imaginaria;
}
double Complex::abs() const {
    return sqrt(Complex::real * Complex::real + Complex::imaginaria * Complex::imaginaria);
}

double Complex::arg() const {
    return atan2(Complex::real, Complex::imaginaria);
}

Complex* Complex::soma(const Complex *other) const {
    double realPart = Complex::real + other->getParteReal();
    double imaginaryPart = Complex::imaginaria + other->imaginaria;

    return new Complex(realPart, imaginaryPart);
}

Complex* Complex::sub(const Complex *other) const {
    double realPart = Complex::real - other->getParteReal();
    double imaginaryPart = Complex::imaginaria - other->imaginaria;

    return new Complex(realPart, imaginaryPart);
}
Complex* Complex::mult(const Complex *other) const {
    double realPart = (Complex::real * other->getParteReal()) - (Complex::imaginaria * other->imaginaria);
    double imaginaryPart = (Complex::real * other->imaginaria) + (Complex::imaginaria * other->getParteReal());

    return new Complex(realPart, imaginaryPart);
}

Complex* Complex::div(const Complex *other) const {

    double realPart = Complex::abs() / other->abs();
    double imaginaryPart = Complex::arg() - other->arg();
    return new Complex(realPart, imaginaryPart);
}

std::string Complex::toString(const int modo) const
{
    double angle;
    std::stringstream buffer;
    if(modo == RET){
        buffer << "(" << real << ", " << imaginaria << ")";
    }
    else{
        angle = Complex::arg() * 180.0 /3.1415;
        buffer << "(" << Complex::abs() << "<" <<angle<<")";
    }
    return buffer.str();
}