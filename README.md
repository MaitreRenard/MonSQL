# MonSQL

Langage Structuré de Demande en français

## TODO
* Créer une Erreur Voltaire
```python
class ErreurVoltaire(Error):
	"""Lancer lorsqu'il y a une erreur dans la syntaxe"""
	pass
```

## Build de MySQL

Les sources de MySQL 5.7.28 sont dans le dossier `mysql`.

1. Récupération des sources

[MySQL Server](https://github.com/mysql/mysql-server.git)

2. Installation des dépendances

Il faut installer :
* cmake
* cmake-boost
* bison

3. Construction

```bash
mkdir <dossier_build>
cd <dossier_build>
cmake ..
make
make install #sudo peut être nécessaire
```


## Tableau de correspondance

| SQL             | MonSQL                       | 
|-----------------|------------------------------| 
| ABS             | LARACINEDUCARREDE            | 
| ALL             | LINTEGRALITEDE               | 
| ALTER           | MODIFIE                      | 
| AND             | AINSIQUE                     | 
| ANY             | LUNDES                       | 
| AS              | CONNUSOUSLENOMDE             | 
| AUTO\_INCREMENT | INCREMENTATIONAUTOMATIQUE    | 
| AVG             | MOYENNE                      | 
| BETWEEN         | INTERCALERENTRE              | 
| CHAR            | CARACTERE                    | 
| CHECK           | VERIFIEQUE                   | 
| COMMIT          | COMMETTRE                    | 
| CONCAT          | ASSEMBLER                    | 
| CONSTRAINT      | CONTRAINTE                   | 
| COUNT           | DENOMBRE                     | 
| CREATE          | CREATIONDE                   | 
| CROSSJOIN       | JOINTURECROISEE              | 
| CROSSJOIN       | JOINTURECROISEE              | 
| DATABASE        | LABASEDEDONNEE               | 
| DELETE          | SUPPRIME                     | 
| DISTINCT        | SANSDUPLICATIONS             | 
| DIVIDE          | DIVISEPAR                    | 
| DROP            | JETTE                        | 
| EXISTS          | ESTPRESENTDANS               | 
| FOREIGN KEY     | CLEFPASDECHEZNOUS            | 
| FROM            | APARTIRDE                    | 
| GREATEST        | LEPLUSGRANDDE                | 
| GROUPBY         | REGROUPERPAR                 | 
| HAVING          | AYANT                        | 
| IF              | SI                           | 
| IN              | DEDANS                       | 
| INNERJOIN       | JOINTUREDUDEDANS             | 
| INSERT          | INSERER                      | 
| INT             | ENTIER                       | 
| INTERSECT       | ENTRECOUPEMENT               | 
| INTO            | ALINTERIEUR                  | 
| IS              | EST                          | 
| IS              | EST                          | 
| LEAST           | LEPLUSPETITDE                | 
| LEFT JOIN       | JOINTUREGAUCHE               | 
| LENGTH          | TAILLEDE                     | 
| LIKE            | SEMBLABLEA                   | 
| LOWER           | MINUSCULER                   | 
| MAX             | LECULMINANTDE                | 
| MIN             | LEMOINDREDE                  | 
| MINUS           | ALADIFFERENCEDE              | 
| NOT             | PAS                          | 
| NULL            | NÉANT                        | 
| NUMBER          | NOMBRE                       | 
| ON              | LORSQUELON                   | 
| ORDERBY         | ORDONNERPAR                  | 
| OR              | OUBIEN                       | 
| POWER           | PUISSANCE                    | 
| PRIMARY KEY     | CLEF                         | 
| RESTRICT        | EMPECHE                      | 
| RIGHT JOIN      | JOINTUREDROITE               | 
| ROLLBACK        | RETOURENARRIERE              | 
| ROUND           | LARRONDIDE                   | 
| SAVEPOINT       | POINTDESAUVEGARDE            | 
| SELECT          | SELECTIONNE                  | 
| SET             | DEFINIT                      | 
| SLEEP           | DORMIR                       | 
| SUM             | ADDITIONDETOUT               | 
| TABLE           | LATABLE                      | 
| TRUNCATE        | TRONQUE                      | 
| UNION           | MISEENCONCUBINAGE            | 
| UPDATE          | METAJOUR                     | 
| UPPER           | MAJUSCULER                   | 
| USE             | UTILISE                      | 
| VALUES          | VALEURS                      | 
| VARCHAR2        | CARACTEREVARIABLEVERSIONDEUX | 
| VOID            | VIDE                         | 
| WHERE           | OÙ                           | 
| #               | CROISILLON                   | 
| =               | VAUT                         | 
| <>              | NEVAUTPAS                    | 
| <               | STRICTEMENTINFERIEURA        | 
| >               | STRICTEMENTSUPERIEURA        | 
| <=              | INFERIEUROUVAUT              | 
| >=              | SUPERIEUROUVAUT              | 
| SYSDATE         | MAINTENANT                   | 
| ,               | ET                           | 

