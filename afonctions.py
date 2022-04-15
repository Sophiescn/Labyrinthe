import fltk
import bouton


def sur_bouton(bouton, click):
    """
    La fonction prend en argument un bouton et l'endroit ou le joueur a
    cliquer et renvoi si le joueur a cliquer sur le bouton.

    Parameters
    ----------
    bouton : Liste
        liste de deux coordonnees.

    click : Liste
        liste de deux coordonnees.

    Returns
    -------
    True ou False.

    >>> sur_bouton([0, 0, 10, 10], [5, 3])
    True
    >>> sur_bouton([0, 0, 10, 10], [12, 5])
    False
    >>> sur_bouton([0, 0, 10, 10], [10, 10])
    True
    """
    top_x = bouton[0]
    top_y = bouton[1]
    bas_x = bouton[2]
    bas_y = bouton[3]
    return top_x <= click[0] <= bas_x and top_y <= click[1] <= bas_y


def rectangle(bouton, ep, t, c):
    top_x = bouton[0]
    top_y = bouton[1]
    bas_x = bouton[2]
    bas_y = bouton[3]
    fltk.rectangle(top_x, top_y, bas_x, bas_y, epaisseur=ep, tag=t, couleur=c)


def chemin(dico):
    """
    perrmet l'affichage du labyrinthe
    dessiner par le module fltk

    Parametres
    ----------
    mouv[0] gauche
    mouv[1] droite
    mouv[2] devant
    mouv[3] deriere
    mouv[4] loin_gauche
    mouv[5] loin_droite
    mouv[6] loin_devant
    mouv[7] loin_deriere
    """

    mouv = dico['a_mouv']

    fltk.rectangle(0, 300, 400, 0, epaisseur=5)

    if mouv[0]:
        fltk.ligne(0, 270, 40, 270)  # gauche proche ouvert BAS
        fltk.ligne(40, 270, 40, 30)
        fltk.ligne(0, 30, 40, 30)  # gauche proche ouvert HAUT
    else:
        # si gauche est ferme
        fltk.ligne(0, 300, 40, 270)
        fltk.ligne(0, 0, 40, 30)
        fltk.ligne(40, 270, 40, 30)

    if mouv[1]:
        fltk.ligne(400, 270, 360, 270)
        fltk.ligne(360, 270, 360, 30)
        fltk.ligne(360, 30, 400, 30)  # droite proche ouvert HAUT

    else:
        # si droite est ferme
        fltk.ligne(400, 300, 360, 270)
        fltk.ligne(400, 0, 360, 30)
        fltk.ligne(360, 270, 360, 30)

    if not mouv[2]:
        fltk.rectangle(40, 30, 360, 270)

    else:
        if mouv[4]:
            fltk.rectangle(120, 90, 40, 210)
        else:
            # si gauche est ferme
            fltk.ligne(40, 270, 120, 210)
            fltk.ligne(40, 30, 120, 90)
            fltk.ligne(120, 210, 120, 90)

        if mouv[5]:
            fltk.rectangle(360, 90, 280, 210)

        else:
            # si droite est ferme
            fltk.ligne(360, 270, 280, 210)
            fltk.ligne(360, 30, 280, 90)
            fltk.ligne(280, 210, 280, 90)

        if mouv[8]:
            fltk.rectangle(152, 120, 184, 210)
            fltk.rectangle(184, 120, 216, 210)

        if mouv[6]:
            fltk.ligne(120, 90, 140, 110)
            fltk.ligne(120, 210, 140, 190)
            fltk.ligne(280, 90, 260, 110)
            fltk.ligne(280, 210, 260, 190)
        else:
            fltk.rectangle(120, 90, 280, 210)


def efface(numero, image):
    """
    la fonction permet d'effacer l'ecran et dessiner le menu

    Parameters
    ----------
    numero : str
        c'est le numero de la carte que le joueur a choisi
    image : str
        l'image qui sert de fond.

    Returns
    -------
    None.

    """
    fltk.efface_tout()
    fltk.image(350, 250, image, ancrage='center')
    fltk.texte(0, 0, 'Jouer', ancrage='nw', taille=30)

    rectangle(bouton.buttons['boutons'][0], 6, '1', 'black')
    fltk.texte(185, 44, '1', ancrage='center', taille=50)

    rectangle(bouton.buttons['boutons'][1], 6, '2', 'black')
    fltk.texte(440, 44, '2', ancrage='center', taille=50)

    rectangle(bouton.buttons['boutons'][2], 6, '3', 'black')
    fltk.texte(55, 155, '3', ancrage='center', taille=50)

    rectangle(bouton.buttons['boutons'][3], 6, '4', 'black')
    fltk.texte(305, 155, '4', ancrage='center', taille=50)

    rectangle(bouton.buttons['boutons'][4], 6, '5', 'black')
    fltk.texte(565, 155, '5', ancrage='center', taille=50)

    rectangle(bouton.buttons['boutons'][5], 6, '9', 'black')
    fltk.texte(78, 450, 'Bonus', ancrage='center', taille=42)

    rectangle(bouton.buttons['boutons'][6], 6, '10', 'green')
    fltk.texte(601, 40, 'TUTORIEL', ancrage='center',
               taille=28, couleur='green')

    fltk.efface(numero)

    if numero == '1':
        rectangle(bouton.buttons['boutons'][0], 6, '1', 'purple')

    elif numero == '2':
        rectangle(bouton.buttons['boutons'][1], 6, '2', 'purple')

    elif numero == '3':
        rectangle(bouton.buttons['boutons'][2], 6, '3', 'purple')

    elif numero == '4':
        rectangle(bouton.buttons['boutons'][3], 6, '4', 'purple')

    elif numero == '5':
        rectangle(bouton.buttons['boutons'][4], 6, '5', 'purple')

    elif numero == '9':
        rectangle(bouton.buttons['boutons'][5], 6, '9', 'purple')


def choix():
    """
    la fonction permet au joueur de decider s'il veut 
    recommencer une partie ou s'il veut en continuer une deja entame

    """
    fltk.efface_tout()
    fltk.texte(350, 200, 'Voulez vous commencer \n une nouvelle partie ?',
               ancrage='center', taille=45)
    fltk.rectangle(80, 380, 210, 450, epaisseur=3, couleur='darkgreen')
    fltk.rectangle(400, 380, 530, 450, epaisseur=3, couleur='darkred')
    fltk.texte(145, 415, 'Oui', ancrage='center',
               taille=30, couleur='darkgreen')
    fltk.texte(465, 415, 'Non', ancrage='center',
               taille=30, couleur='darkred')
    fltk.mise_a_jour()
    ouibtn = [80, 380, 210, 450]
    nonbtn = [400, 380, 530, 450]
    while True:
        pouet = fltk.attend_clic_gauche()
        if sur_bouton(ouibtn, pouet):
            return True
        elif sur_bouton(nonbtn, pouet):
            fltk.efface_tout()
            fltk.texte(350, 250,
                       'Vos stickers sont réinitialiser.\nBonne chance',
                       ancrage='center', taille=50)
            fltk.mise_a_jour()
            return False


def affiche_stickers(dico):
    """
    la fonction permet d'afficher les differents stickers que
    le joueur a pu placer.

    Parameters
    ----------
    dico : dictionaire
        dictionaire du jeu.

    Returns
    -------
    None.

    """
    x = dico['position'][0][0]
    y = dico['position'][0][1]
    if [x, y] in dico['ronds']:
        fltk.cercle(30, 350, 30, remplissage='darkred', couleur='darkred')
        fltk.ligne(14, 335, 44, 365, couleur='white')
        fltk.ligne(14, 365, 44, 335, couleur='white') 