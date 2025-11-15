#!/usr/bin/python3
def pow(a, b):
    result = 1
    exponent = abs(b)  # müsbət dərəcəyə çevir
    for _ in range(exponent):
        result *= a
    if b < 0:
        return 1 / result  # mənfi qüvvə üçün tərsini qaytar
    return result
