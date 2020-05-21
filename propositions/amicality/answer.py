#-------------------------------------------------------------------------------
# Name:        answer
# Purpose:     Solution de ma proposition amicality
#
# Author:      Nelson
#
# Created:     19/05/2020
# Copyright:   (c) HP 2020
# Licence:     Creative Commons
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class Member:
    """
        Representation d'un membre du devc
        Attributes:
            nom: chaine de caractere representant le nom du membre
            friends: un ensemble contenant le nom de tous les amis du membre
            ia: nombre designant l'amicalite interieure du membre
            ea: nombre designant l'amicalite exterieure du membre
    """
    def __init__(self, nom):
        self.nom = nom
        self.friends = set()
        self.ia = 0
        self.ea = 0

class Devc:
    """
        Representation d'un DevC
        Attributes:
            length: nombre designant le nombre de membre du DevC
            links: list contenant tous les membres du DevC
            members: list contenant le nom de tous les membres du DevC
    """
    def __init__(self, n):
        self.length = n
        self.links = []
        self.members = []

def eamicality(member, others):
    """
        Calcule l'amicalite exterieur d'un membre, ne retourne rien, modifie
        directement l'attribut ia du membre
        Parameters:
            member: Member le membre dont on souhaite calculer l'amicalite exterieur
            others: liste de noms des membres du DevC
    """

    maxcommon = 0
    ncommon = 0

    for el in others:
        ncommon = len(member.friends & el.friends)
        if maxcommon < ncommon:
            maxcommon = ncommon

    member.ea = maxcommon

def iamicality(member, others):
    """
        Calcule l'amicalite interieur d'un membre, ne retourne rien, modifie
        directement l'attribut ia du membre
        Parameters:
            member: Member le membre dont on souhaite calculer l'amicalite interieur
            others: liste des autres membres du DevC
    """

    for friend in member.friends:
        if friend in others:
            member.ia += 1

def tamicality(devc):
    """
        Calcule l'amicalité totale d'un DevC
        devc: Devc une instance du Devc dont on souhaite calculer l'amicalite
    """

    for member in devc.links:
        iamicality(member, devc.members)

    for i in range(devc.length):
        eamicality(devc.links[i], devc.links[:i] + devc.links[i+1:])

    ia, ea = 0, 0

    for member in devc.links:
        ia += member.ia
        ea += member.ea

    return ia, ea, ia+ea

def main():

    #Recuperation des donnees
##    N = int(input())
##    devc = Devc(N)
##
##    for i in range(N):
##        line = input()
##        C, M = line.split(' ')[0], int(line.split(' ')[1])
##        devc.members.append(C)
##        devc.links.append(Member(C))
##
##        for j in range(M):
##            friend = input()
##            devc.links[i].friends.add(friend)
##
##    print(*tamicality(devc))

    #Recuperation des donnees au travers d'un fichier pour lests

    test = "test2.txt"
    with open(test, 'r') as file:
        N = int(file.readline())
        devc = Devc(N)

        for i in range(N):
            line = file.readline()
            C, M = line.split(' ')[0], int(line.split(' ')[1])
            devc.members.append(C)
            devc.links.append(Member(C))

            for j in range(M):
                friend = file.readline()[:-1]
                devc.links[i].friends.add(friend)

        print(*tamicality(devc))

if __name__ == '__main__':
    main()

