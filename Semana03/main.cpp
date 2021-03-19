//
// Created by guilherme on 18/03/2021.
//

#include <iostream>

#include "complexo.h"

int main(int argc, char** argv)
{
    using namespace std;
    double realPart = 1;
    double imaginaryPart = 1;

    Complex* complex1 = new Complex(realPart, imaginaryPart, RET);

    realPart = 2;
    imaginaryPart =2;

    Complex* complex2 = new Complex(realPart, imaginaryPart, RET);

    Complex* complex3 = complex1->soma(complex2);

    Complex* complex4 = complex1->sub(complex2);

    Complex* complex5 = complex1->mult(complex2);

    Complex* complex6 = complex1->div(complex2);

    cout << complex1->toString(RET) << " + " << complex2->toString(RET)
         << " = " << complex3->toString(RET) << endl;

    cout << complex1->toString(RET) << " - " << complex2->toString(RET)
         << " = " << complex4->toString(RET) << endl;

    cout << complex1->toString(RET) << " * " << complex2->toString(RET)
         << " = " << complex5->toString(RET) << endl;

    cout << complex1->toString(RET) << " / " << complex2->toString(RET)
         << " = " << complex6->toString(RET) << endl;

    cout << "Numeros na forma polar: \n" << endl;

    cout << complex1->toString(POLAR) << " + " << complex2->toString(POLAR)
         << " = " << complex3->toString(POLAR) << endl;

    cout << complex1->toString(POLAR) << " - " << complex2->toString(POLAR)
         << " = " << complex4->toString(POLAR) << endl;

    cout << complex1->toString(POLAR) << " * " << complex2->toString(POLAR)
         << " = " << complex5->toString(POLAR) << endl;

    cout << complex1->toString(POLAR) << " / " << complex2->toString(POLAR)
         << " = " << complex6->toString(POLAR) << endl;

    delete complex1;
    delete complex2;
    delete complex3;
    delete complex4;
    delete complex5;
    delete complex6;

    return 0;
}