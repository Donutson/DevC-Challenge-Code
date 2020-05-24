# Enoncé
Le DevC de ta localité te confie la tâche de calculer son amicalité totale.
Qu'est-ce que l'amicalité totale?
L'un des objectifs d'un DevC est de permettre aux dévéloppeurs d'une localité d'échanger 
et se connaitre, l'amicalité totale permet donc de voir à quel point les membres d'un DevC
sont amis. Tout d'abord il faut savoir qu'il existe 2 types primaires d'amicalité, l'amicalité
intérieure et l'amicalité extérieure; l'amicalité totale est la somme des deux.
Etant données un DevC, on donnne la liste de ses membres et pour chaque membre
on donne la liste de ses amis (les amis peuvent être dans le DevC ou hors du DevC).
L'amicalité intérieure d'un membre est son nombre d'amis étant dans le DevC;
l'amicalité intérieure du DevC est la somme des amicalités intérieure de tous ses membres.
L'amicalité extérieure d'un membre est le maximum d'amis qu'il a en commun avec un autre membre du DevC
(leurs amis en communs peuvent être dans le DevC ou hors du DevC), l'amicalité extérieure du DevC
est la somme des amicalités extérieure de tous ses membres.

# Entrées
Une ligne contenant le nombre N de membres du DevC, ensuite N sections,
chaque section commence par une ligne contenant une chaine de caractère C et un nombre M
séparé par un espace, C représente le nom du membre et M son nombre d'amis; cette ligne est suivit
par M lignes contenant chacune une chaine de caractère représentant le nom d'un ami de C.

# Sortie
L'amicalité intérieure I, extérieure E et totale T du DevC séparé par des espaces

# Exemple 1
```
Entrées              Sortie
2                    2 4 6
Mike 3
Sarah
Jhon
Michel
Jhon 6
Mike
Franck
Sery
Michel
Yannick
Sarah
```
# Exemple 2
```
Entrées              Sortie
3                    4 6 10
Jean 3
Patrick
Noe
Joel
Fabrice 2
Joel
Noe
Joel 4
Jean
Noe
Patrick
Fabrice
```
# Exemple 3
```
Entrées               Sortie
10                    17 15 32
Jean 3
Patrick
Noe
Joel
Fabrice 1
Noe
Joel 4
Jean
Brice
Patrick
Joelle
Jacques 5
Pierre
Romeo
Sean
Boa
Simeon
Simeon 5
Patrick
Noe
Brigitte
Prince
Jacques
Pierre 3
Jacques
George
Leo
Brigitte 2
Paul
Simeon
Sean 1
Brice
Patrick 5
Simeon
Jean
Joel
Marie
George
Prince 3
Boa
Simeon
Marie<
```
