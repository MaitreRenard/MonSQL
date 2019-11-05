#!/usr/bin/env python3
# coding: utf-8

keywords = { "BETWEEN":"INTERCALERENTRE",
"IN":"DEDANS",
"SELECT":"SELECTIONNE",
"NOT":"PAS",
"ORDER BY":"ORDONNERPAR",
"GROUP BY":"REGROUPERPAR",
"HAVING":"AYANT",
"OR":"OUBIEN",
"AND":"AINSIQUE",
"LIKE":"SEMBLABLEA",
"INTO":"ALINTERIEUR",
"DISTINCT":"SANSDUPLICATIONS",
"SET":"DEFINIT",
"CHECK":"VERIFIEQUE",
"ROLLBACK":"RETOURENARRIERE",
"COMMIT":"COMMETTRE",
"FROM":"APARTIRDE",
"WHERE":"OÙ",
"DROP":"LACHE",
"ALTER":"MODIFIE",
"INSERT":"INSERER",
"UPDATE":"METAJOUR",
"DELETE":"SUPPRIME",
"VOID":"VIDE",
"NULL":"NÉANT",
"VALUES":"VALEURS",
"AVG":"MOYENNE",
"COUNT":"DENOMBRE",
"CONCAT":"ASSEMBLER",
"TRUNCATE":"TRONQUE",
"SLEEP":"DORMIR",
"UNION":"MISEENCONCUBINAGE",
"SAVEPOINT":"POINTDESAUVEGARDE",
"IS":"EST",
"ALL":"LINTEGRALITE",
"NUMBER":"NOMBRE",
"CHAR":"CARACTERE",
"VARCHAR2":"CARACTEREVARIABLEVERSIONDEUX",
"CROSS JOIN":"JOINTURECROISEE",
"INNER JOIN":"JOINTUREDUDEDANS",
"NATURAL JOIN":"JOINTURENATURELLE",
"=":"VAUT",
">=":"SUPERIEUROUVAUT",
"<=":"INFERIEUROUVAUT",
"<>":"NEVAUTPAS",
"#":"CROISILLON" }


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

uIn = 0
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
