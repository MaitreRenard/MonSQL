#!/usr/bin/env python3
# coding: utf-8

def toFrench(query: str):
    for key in keywords:
        if key in query:
            query = query.replace(key,keywords[key])

    return query

def toSQL(query: str):
    for key, value in keywords.items():
        if value in query:
            query = query.replace(value,key)

    return query

def printMenu():
    print("[1] Traduire en MonSQL")
    print("[2] Traduire en MySQL")
    print("[3] Quitter")

def readCSV(filename: str):
    with open(filename,'r') as f:
        fileContent = f.readlines()
        dic = {}

        for line in fileContent:
            key, value = line.strip().split(';')
            dic[' ' + key + ' '] = ' ' + value + ' '

    return dic

uIn = 0
keywords = readCSV("../keywords.csv")
while uIn != 3:
    printMenu()
    uIn = int(input())
    if uIn == 1 or uIn == 2:
        print("Entrez votre requête")
        if uIn == 1:
            print(toFrench(input()))
        else:
            print(toSQL(input()))
        print()
