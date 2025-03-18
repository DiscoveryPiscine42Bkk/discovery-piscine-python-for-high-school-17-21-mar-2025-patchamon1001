#!/usr/bin/env python3
k= 0
while k<=10:
    print(f"Table de {k}: ", end="")
    count =0
    while count <=10:
       print(k* count ,end=' ')
       count+=1
    k+=1
    print()