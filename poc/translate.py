#!/usr/bin/env python3
# coding: utf-8

import argparse

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

def readCSV(filename: str):
    with open(filename,'r') as f:
        fileContent = f.readlines()
        dic = {}

        for line in fileContent:
            key, value = line.strip().split(';')
            dic[' ' + key + ' '] = ' ' + value + ' '

    return dic

# Premièrement, mettre en place les mots clés
keywords = readCSV("../keywords.csv")
parser = argparse.ArgumentParser()
parser.add_argument("langageDestination", help="Le langage vers lequel vous voulez traduire")
parser.add_argument("toTranslate", help="La chaîne de caractère à traduire")
parser.add_argument("-f","--file", help="Fichier à traduire")
args = parser.parse_args()

args.langageDestination = args.langageDestination.lower()
translated = ''

if args.langageDestination == 'monsql':
    if args.file is not None:
        with open(args.file,'r') as f:
            fileContent = f.read()
        translated = toFrench(fileContent)
    else:
        translated = toFrench(args.toTranslate)
    print(translated)
elif args.langageDestination == 'mysql':
    if args.file is not None:
        with open(args.file,'r') as f:
            fileContent = f.read()
        translated = toSQL(fileContent)
    else:
        translated = toSQL(args.toTranslate)
    print(translated)
else:
    print("Je n'ai pas compris en quel langage vous voulez traduire votre chaîne de caractère")
