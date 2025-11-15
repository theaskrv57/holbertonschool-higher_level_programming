#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # Əgər simvol kiçik hərfdirsə
        if ord('a') <= ord(char) <= ord('z'):
            # Böyük hərfə çevirmək üçün 32 çıxırıq
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
