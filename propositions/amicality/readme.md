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

# Sorties
L'amicalité intérieure I, extérieure E et totale T du DevC séparé par des espaces

# Exemple 1

Entrées              Sortie<br>
3                    3 5 8<br>
Jean 3<br>
Patrick<br>
Noe<br>
Joel<br>
Fabrice 1<br>
Noe<br>
Joel 4<br>
Jean<br>
Noe<br>
Patrick<br>
Fabrice<br>

# Exemple 2<br>

Entrées               Sortie<br>
10                    14 14 28<br>
Jean 3<br>
Patrick<br>
Noe<br>
Joel<br>
Fabrice 1<br>
Noe<br>
Joel 4<br>
Jean<br>
Brice<br>
Patrick<br>
Joelle<br>
Jacques 4<br>
Romeo<br>
Sean<br>
Boa<br>
Simeon<br>
Simeon 3<br>
Patrick<br>
Noe<br>
Jacques<br>
Pierre 3<br>
Jacques<br>
George<br>
Leo<br>
Brigitte 2<br>
Paul<br>
Simeon<br>
Sean 1<br>
Brice<br>
Patrick 5<br>
Simeon<br>
Jean<br>
Joel<br>
Marie<br>
George<br>
Jacques 3<br>
Boa<br>
Simeon<br>
