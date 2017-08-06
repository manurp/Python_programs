# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        r = self.real + no.real
        im = self.imaginary + no.imaginary
        return Complex(r, im)

    def __sub__(self, no):
        r = self.real - no.real
        im = self.imaginary - no.imaginary
        return Complex(r, im)

    def __mul__(self, no):
        ''' (a+jb)*(c+jd) = a*c + j*b*c + j*a*d - b*d '''
        r = self.real * no.real - self.imaginary * no.imaginary
        im = self.imaginary * no.real + self.real * no.imaginary
        return Complex(r, im)

    def __truediv__(self, no):
        ''' (a+jb)/(c+jd) -> divide by rationalization'''
        r = (self.real * no.real + self.imaginary * no.imaginary) / (no.real**2 + no.imaginary**2)
        im = (self.imaginary * no.real - self.real * no.imaginary) / (no.real**2 + no.imaginary**2)
        return Complex(r, im)

    def mod(self):
        # return '%.2f+0.00i' % math.sqrt(self.real**2 + self.imaginary**2)
        return '{0:.2f}+0.00i'.format(math.sqrt(self.real**2 + self.imaginary**2))
        #real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        # return Complex(real, 0)

    def __str__(self):
        # if self.imaginary == 0:
        #     result = "%.2f+0.00i" % (self.real)
        # elif self.real == 0:
        #     if self.imaginary >= 0:
        #         result = "0.00+%.2fi" % (self.imaginary)
        #     else:
        #         result = "0.00-%.2fi" % (abs(self.imaginary))
        # elif self.imaginary > 0:
        #     result = "%.2f+%.2fi" % (self.real, self.imaginary)
        # else:
        #     result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        # return result
        return '{0:.2f}{1:+.2f}i'.format(self.real, self.imaginary)


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
    # print(x + y)
