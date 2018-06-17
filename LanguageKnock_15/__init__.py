# coding: utf-8

import codecs
import re

def parseInt(n):
    while(True):
        try:
            return int(n)
        except ValueError:
            print('整数を入力')
            n=input("n= ")


#ファイル読み出し
ifile = codecs.open('D:\hightemp.txt', 'r','utf-8')
lines=ifile.readlines()

#出力する行数を入力
n=input("n= ")
intN=parseInt(n)

olines=len(lines)-intN

for i in range(olines,len(lines)):
    print (lines[i],end='')
