def carte1():
    name = 'carte1.txt'
    carte = open(name, 'w')
    carte.write('******' + '\n' + '*....*' + '\n' + '**.*.*' + '\n' +
                '**.*X*' + '\n' + '**@***' + '\n')
    carte.close()
    return name


def carte2():
    carte = 'carte2.txt'
    carte2 = open(carte, 'w')
    carte2.write('********' + '\n' + '....**' + '\n' + '*.*.X*' +
                 '\n' + '*.***.' + '\n' + '*.....' + '\n' + '***@**' + '\n')
    carte2.close()
    return carte


def carte3():
    carte = 'carte3.txt'
    carte3 = open(carte, 'w')
    carte3.write('*******' + '\n' + '*...*..' + '\n' + '*.***.*' + '\n' +
                 '*..*..*' + '\n' + '**...**' + '\n' + '***.***' + '\n' +
                 '*...***' + '\n' + 'X.*...@' + '\n')
    carte3.close()
    return carte


def carte4():
    carte = 'carte4.txt'
    carte4 = open(carte, 'w')
    carte4.write('**.....***' + '\n' + '*..***.*.X' + '\n' + '**...*...*' +
                 '\n' + '*.**.**.**' + '\n' + '*....**.**' + '\n' +
                 '*.**...***' + '\n' + '*.**@*.***' + '\n')
    carte4.close()
    return carte


def carte5():
    carte = 'carte5.txt'
    carte5 = open(carte, 'w')
    carte5.write('**********' + '\n' + '..****...*' + '\n' + '.*.....*.*' +
                 '\n' + '..*.***...' + '\n' + '*....****.' + '\n' +
                 '...*..***.' + '\n' + '@****....X' + '\n')
    carte5.close()
    return carte


def bonus():
    carte = 'bonus.txt'
    bonus = open(carte, 'w')
    bonus.write('X..*..*****' + '\n' + '**.**.**.**' + '\n' + '*..*...***.' +
                '\n' + '*.*.**.*..*' + '\n' + '..*.*..**.*' +
                '\n' + '.**.*.***.*' + '\n' + '....*..*..*' +
                '\n' + '*.**.*.*.**' + '\n' + '*.*......**' +
                '\n' + '*.**.**.***' + '\n' + '*.**.*..**.' +
                '\n' + '*.**.*.*...' + '\n' + '*....*...**' +
                '\n' + '***.****.**' + '\n' + '..*.***....' +
                '\n' + '*.*.***.**.' + '\n' + '*...***.**.' +
                '\n' + '***.....*..' + '\n' + '*****.*.*.*' +
                '\n' + '.***..*...*' + '\n' + '.....*..***' +
                '\n' + '**.***.****' + '\n' + '*..*.*.****' +
                '\n' + '**..@..****' + '\n')
    bonus.close()
    return carte


def copy_doc(source, dest):  # dest = destination
    """
    la fonction copie une document texte dans un autre.

    Parameters
    ----------
    source : str
        fichier.txt.
    dest : str
        fichier.txt.

    Returns
    -------
    None.

    """
    doc = open(source, 'r')
    lignes = doc.readlines()
    doc.close()
    user = open(dest, 'w')
    for i in lignes:
        user.write(i)
    user.close()


def init_cartes():
    """
    Cree les cartes sur le repertoire de jeu

    Returns
    -------
    None.

    """
    carte1()
    carte2()
    carte3()
    carte4()
    carte5()
    bonus()


maze_files = ['carte1.txt', 'carte2.txt', 'carte3.txt', 'carte4.txt',
              'carte5.txt', 'bonus.txt']
# nous partons du principe que l'utilisateur veut conserver sa progression 
# dans tous les niveaux
bonus_carte = 6


def quelle_carte(numero, restart):
    """
    la fonction retourne le nom du fichier dans lequel le joueur 
    va progresser.

    Parameters
    ----------
    numero : int
        c'est le numero de la carte que le joueur a choisi
    restart : booleen
        True si le joueur veut commencer une nouvelle partie.

    Returns
    -------
    j_file : str
        lien vers le document texte de la carte.

    """

    if restart:
        if numero == 9:
            j_file = 'user_bonus.txt'
            doc_source = 'bonus.txt'
        else:
            j_file = 'user' + maze_files[numero - 1]
            doc_source = maze_files[numero - 1]
        copy_doc(doc_source, j_file)
    else:
        if numero == 9:
            j_file = 'user_bonus.txt' 
        else: 
            j_file = 'user' + maze_files[numero - 1]

    return j_file