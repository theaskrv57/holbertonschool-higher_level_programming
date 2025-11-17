#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # 1-ci elementdən başlayaraq bütün arqumentləri götürürük, script adı çıxılır
    num_args = len(args)  # arqumentlərin sayını hesablayırıq

    if num_args == 0:
        print("0 arguments.")  # heç bir arqument yoxdursa
    else:
        print(f"{num_args} argument{'s' if num_args > 1 else ''}:")  # 1 arqument varsa "argument", bir neçə varsa "arguments"
        for i, arg in enumerate(args, start=1):  # arqumentləri nömrələyərək dövrəyə alırıq
            print(f"{i}: {arg}")  # 1: Hello, 2: Welcome və s.
