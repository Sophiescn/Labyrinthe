def separe_lignes(ligne):
    """
    la fonction prend en agument une chaine de caractere et en separe les
    differents elements dans une liste.

    Parameters
    ----------
    ligne : chaine de charactere


    Returns
    -------
    une liste de characteres.

    >>> separe_lignes('******')
    ['*', '*', '*', '*', '*', '*']
    >>> separe_lignes('')
    []
    >>> separe_lignes('**...*')
    ['*', '*', '.', '.', '.', '*']

    """
    lst = []
    for char in ligne:
        if char == '\n':
            continue
        lst.append(char)
    return lst


def ligne_vers_tableau(carte):
    """
    la fonction prends en argument le document texte dans lequel est le
    labirynthe (maze) et fabrique une liste de liste avec chacun des
    caracteres.

    Parameters
    ----------
    carte : document texte
        document dans le dossier dans lequel est sauvergarder le fichier.

    Returns
    -------
    liste de liste.



    """
    doc = open(carte, 'r')
    lignes = doc.readlines()
    maze = []  # maze = labyrinthe
    for ligne in lignes:
        maze.append(separe_lignes(ligne))
    doc.close()
    return maze


def position(dico):
    """
    la fontion va trouver la position du joueur represente par une @ et la
    renvoyer.

    Parameters
    ----------
    dico : dictionaire.

    Returns
    -------
    une liste avec les coordonnees de @ .

    >>> maze = [['*', '*', '*', '*', '*'], ['*', '.', '.', '.', '*'], ['*', '@', '*', '*', '*'], ['*', '.', '*', '*', '*']]
    >>> exemple = {'maze' : maze}
    >>> position(exemple)
    [[1, 2], [5, 4]]
    >>> maze = [['*', '*', '*', '*', '*'], ['*', '.', '.', '.', '.'], ['*', '.', '*', '*', '*'], ['*', '.', '*', '*', '*']]
    >>> exemple = {'maze' : maze}
    >>> position(exemple)
    []
    >>> maze = [['*', '*', '*', '*', '*'], ['*', '.', '.', '.', '.'], ['*', '.', '*', '*', '*'], ['*', '.', '*', '*', '@']]
    >>> exemple = {'maze' : maze}
    >>> position(exemple)
    [[4, 3], [5, 4]]

    """
    lignes = len(dico['maze'])
    for y in range(lignes):
        colones = len(dico['maze'][y])
        for x in range(colones):
            if dico['maze'][y][x] == '@':
                return [[x, y], [colones, lignes]]
    return []


def mouvement_autoriser(dico):
    """
    la fonction verifie si des mouvements sont possible et dans quelle
    direction.
    mouv[0] gauche
    mouv[1] droite
    mouv[2] devant
    mouv[3] deriere
    mouv[4] loin_gauche
    mouv[5] loin_droite
    mouv[6] loin_devant
    mouv[7] loin_deriere
    Parameters
    ----------
    dico : dictionaire

    Returns
    -------
    liste de booleens, dans l'ordre movement a gauche, a droite, devant,
    derriere.

    >>> maze = [['*', '*', '*', '*', '*'], ['*', '.', '.', '.', '*'], ['*', '@', '*', '*', '*'], ['*', '.', '*', '*', '*']]
    >>> positions = [[1, 2], [5, 4]]
    >>> mouvement_autoriser({'maze' : maze, 'position' : positions})
    [False, False, True, True, False, True, False, True, False]

    >>> maze = [['*', '*', '*', '*', '*'], ['*', '.', '.', '.', '.'], ['*', '.', '*', '*', '*'], ['*', '.', '*', '*', '@']]
    >>> positions = [[4, 3], [5, 4]]
    >>> mouvement_autoriser({'maze' : maze, 'position' : positions})
    [False, False, False, False, False, False, False, False, False]

    """
    ok_mouvs = ['.', 'X']
    fin = ['X']
    mouv = [False] * 9
    if not dico['position']:
        return mouv
    x = dico['position'][0][0]  # x de la pos
    y = dico['position'][0][1]  # y de la pos
    colones = dico['position'][1][0]
    lignes = dico['position'][1][1]

    # mouvement a gauche :
    mouv[0] = x > 0 and dico['maze'][y][x - 1] in ok_mouvs
    # mouvement a droire :
    mouv[1] = x < (colones - 1) and dico['maze'][y][x + 1] in ok_mouvs
    # mouvement en avant :
    mouv[2] = y > 0 and dico['maze'][y - 1][x] in ok_mouvs
    # mouvement vers le bas :
    mouv[3] = y < (lignes - 1) and dico['maze'][y + 1][x] in ok_mouvs

    mouv[8] = y > 0 and dico['maze'][y - 1][x] in fin

    if mouv[2]:
        # mouvement suivant
        x = x
        y -= 1
        mouv[4] = x > 0 and dico['maze'][y][x - 1] in ok_mouvs
        # mouvement a droire :
        mouv[5] = x < (colones - 1) and dico['maze'][y][x + 1] in ok_mouvs
        # mouvement en avant :
        mouv[6] = y > 0 and dico['maze'][y - 1][x] in ok_mouvs
        # mouvement vers le bas :
        mouv[7] = True
    return mouv


def mouvement(dico):
    """
    la fonction modifie la position du joueur dans le labyrinthe et renvoi
    s'il a gagne ou pas encore.

    Parameters
    ----------
    dico : dictionaire

    Returns
    -------
    True si le joueur a gange  False sinon.


    >>> maze = [['*', '*', '*', '*', '*'], ['*', '.', '.', '.', '*'], ['*', '@', '*', '*', '*'], ['*', '.', '*', '*', '*']]
    >>> pos = [[1, 2], [5, 4]]
    >>> j_mouv = [False, False, True, False]
    >>> exemple = {'maze' : maze, 'position' : pos, 'j_mouv' : j_mouv}
    >>> mouvement(exemple)
    True
    """
    a_mouvs = mouvement_autoriser(dico)
    mouv = dico['j_mouv']

    if mouv[0] == a_mouvs[0] and mouv[0]:
        x_pos = dico['position'][0][0]
        x = x_pos
        y_pos = dico['position'][0][1]
        y = y_pos
        x -= 1
    elif mouv[1] == a_mouvs[1] and mouv[1]:
        x_pos = dico['position'][0][0]
        x = x_pos
        y_pos = dico['position'][0][1]
        y = y_pos
        x += 1
    elif mouv[2] == a_mouvs[2] and mouv[2]:
        y_pos = dico['position'][0][1]
        y = y_pos
        x_pos = dico['position'][0][0]
        x = x_pos
        y -= 1
    elif mouv[3] == a_mouvs[3] and mouv[3]:
        y_pos = dico['position'][0][1]
        y = y_pos
        x_pos = dico['position'][0][0]
        x = x_pos
        y += 1
    else:
        return True

    if dico['maze'][y][x] == 'X':
        return False

    dico['maze'][y][x] = '@'
    dico['maze'][y_pos][x_pos] = '.'
    return True


def maj_maze(dico, carte):
    """
    la fonction va mettre a jour le fichier du labyrinthe.

    Parameters
    ----------
    carte : document texte
        la ou est sauvegarder le labyrinthe.
    dico : dictionaire


    Returns
    -------
    None.

    """
    doc = open(carte, 'w')
    maze = dico['maze']
    lst = []
    for line in maze:  # nombre de lignes
        str = ''
        for x in line:
            str += x
        lst.append(str)
    doc.write('\n'.join(lst))
    doc.close()


def sticker(dico):
    """
    la fonction permet au joueur de placer des stickers
    sur le sol au endroits ou il est deja aller
    """
    x = dico['position'][0][0]
    y = dico['position'][0][1]
    dico['ronds'].append([x, y])
    dico['stickers'] -= 1


def turn_to_left(dico):
    """
    La fonciton permet de faire tourner le labyrinthe.

    Parameter
    ----------
    dico : dictionaire

    Returns
    -------
    le labyrinthe.

    >>> maze = [['*', '*', '*', '*', '*'], ['*', '.', '.', '.', '*'], ['*', '@', '*', '*', '*'], ['*', '.', '*', '*', '*']]
    >>> position = [[1, 2], [5, 4]]
    >>> turn_to_left({'maze' : maze, 'position': position})
    [['*', '*', '*', '*'], ['.', '@', '.', '*'], ['*', '*', '.', '*'], ['*', '*', '.', '*'], ['*', '*', '*', '*']]
    >>> maze = [['*', '*', '*', '*', '*'], ['*', '.', '.', '.', '.'], ['*', '.', '*', '*', '*'], ['*', '.', '*', '*', '@']]
    >>> position = [[4, 3], [5, 4]]
    >>> turn_to_left({'maze' : maze, 'position': position})
    [['*', '*', '*', '*'], ['.', '.', '.', '*'], ['*', '*', '.', '*'], ['*', '*', '.', '*'], ['@', '*', '.', '*']]

    """
    colones = dico['position'][1][0]
    lignes = dico['position'][1][1]
    l1 = []
    l2 = []
    dico['maze'].reverse()
    for x in range(colones):
        for y in range(lignes):
            l1.append(dico['maze'][y][x])
        l2.append(l1)
        l1 = []
    return l2


def turn_to_right(dico):
    """
    La fonction permet de faire tourner le labyrinthe.

    Parameter
    ----------
    dico : dictionaire

    Returns
    -------
    le labyrinthe.

    >>> maze = [['*', '*', '*', '*', '*'], ['*', '.', '.', '.', '*'], ['*', '@', '*', '*', '*'], ['*', '.', '*', '*', '*']]
    >>> position = [[1, 2], [5, 4]]
    >>> turn_to_right({'maze' : maze, 'position': position })
    [['*', '*', '*', '*'], ['*', '.', '*', '*'], ['*', '.', '*', '*'], ['*', '.', '@', '.'], ['*', '*', '*', '*']]
    >>> maze = [['*', '*', '*', '*', '*'], ['*', '.', '.', '.', '.'], ['*', '.', '*', '*', '*'], ['*', '.', '*', '*', '@']]
    >>> position = [[4, 3], [5, 4]]
    >>> turn_to_right({'maze' : maze, 'position': position })
    [['*', '.', '*', '@'], ['*', '.', '*', '*'], ['*', '.', '*', '*'], ['*', '.', '.', '.'], ['*', '*', '*', '*']]
    """
    colones = dico['position'][1][0]
    lignes = dico['position'][1][1]
    l1 = []
    l2 = []
    for x in range(colones):
        for y in range(lignes):
            l1.append(dico['maze'][y][-1 - x])
        l2.append(l1)
        l1 = []
    return l2

