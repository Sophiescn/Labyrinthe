import fltk
import cartes
import afonctions
import fcmaze
import bouton

# constantes

IMAGE = 'labyrinthe.png'  # site de "le RIME"
FLECHE = 'boutons.png'
WIN = 'win.png'


def select_carte():
    numero = ''
    while True:
        click = fltk.attend_clic_gauche()

        if afonctions.sur_bouton(bouton.buttons['play'], click):
            break
        elif afonctions.sur_bouton(bouton.buttons['boutons'][0], click):
            numero = '1'
        elif afonctions.sur_bouton(bouton.buttons['boutons'][1], click):
            numero = '2'
        elif afonctions.sur_bouton(bouton.buttons['boutons'][2], click):
            numero = '3'
        elif afonctions.sur_bouton(bouton.buttons['boutons'][3], click):
            numero = '4'
        elif afonctions.sur_bouton(bouton.buttons['boutons'][4], click):
            numero = '5'
        elif afonctions.sur_bouton(bouton.buttons['boutons'][5], click):
            numero = '9'
        elif afonctions.sur_bouton(bouton.buttons['boutons'][6], click):
            numero = '10'
            break

        afonctions.efface(numero, IMAGE)
        fltk.mise_a_jour()

    return numero


def tutoriel(jeu):
    fltk.efface_tout()
    fltk.image(150, 350, FLECHE, ancrage='nw')
    fltk.rectangle(100, 20, 550, 250, couleur='darkgreen',
                   epaisseur=3, tag='info')
    fltk.texte(325, 85, 
               '    Grâce à ces touches\nvous pourez vous déplacer\n     dans le labyrinthe',
               taille = 28, tag='info', ancrage='center')
    fltk.texte(325, 220, 'OK', taille=40, tag='info', ancrage='center')
    fltk.mise_a_jour()
    while True:
        ev = fltk.attend_clic_gauche()
        ok = [293, 200, 357, 242]
        if afonctions.sur_bouton(ok, ev):
            break
    fltk.efface('info')
    afonctions.chemin(jeu)
    fltk.rectangle(395, 285, 690, 490, epaisseur=7, couleur='darkgreen',
                   tag='info')
    fltk.texte(542, 360,
               "  Ici s'affichera\nla représentation\n   du labyrithe",
               taille=30, ancrage='center', tag='info')
    fltk.texte(542, 450, 'OK', taille=40, tag='info', ancrage='center')
    fltk.mise_a_jour()
    while True:
        ev = fltk.attend_clic_gauche()
        ok = [512, 430, 572, 470]
        if afonctions.sur_bouton(ok, ev):
            break
    fltk.efface('info')
    fltk.rectangle(540, 440, 690, 490, epaisseur=3)
    fltk.texte(615, 465, 'STICKER', ancrage='center', taille=25)
    fltk.rectangle(100, 20, 550, 250, couleur='darkgreen',
                   remplissage='white', epaisseur=3, tag='info')
    fltk.texte(325, 85, 
               'Ce bouton vous permettra\nde marquer un chemin\ndéjà emprunter.',
               taille = 28, tag='info', ancrage='center')
    fltk.texte(325, 160, "Attention vous n'en avez que 3", couleur='darkred',
               ancrage='center', taille=22, tag='info')
    fltk.texte(325, 220, 'OK', taille=40, tag='info', ancrage='center')
    while True:
        ev = fltk.attend_clic_gauche()
        ok = [293, 200, 357, 242]
        if afonctions.sur_bouton(ok, ev):
            break
    fltk.rectangle(100, 20, 550, 250, couleur='darkgreen',
                   remplissage='white', epaisseur=3, tag='info')
    fltk.texte(325, 85,
               "si un stickers a été\nposé il s'affichera ici",
               taille=30, tag='info', ancrage='center')
    fltk.texte(325, 220, 'OK', taille=40, tag='info',
               ancrage='center')
    fltk.ligne(200, 200, 40, 315, epaisseur=3)
    fltk.fleche(200, 200, 40, 315, epaisseur=3)

    fltk.cercle(30, 350, 30, remplissage='darkred',
                couleur='darkred')
    fltk.ligne(14, 335, 44, 365, couleur='white')
    fltk.ligne(14, 365, 44, 335, couleur='white')
    while True:
        ev = fltk.attend_clic_gauche()
        ok = [293, 200, 357, 242]
        if afonctions.sur_bouton(ok, ev):
            break


# programme principal
if __name__ == "__main__":
    # initialisation du jeu
    cartes.init_cartes()
    framerate = 10
    jeu = {'maze': [], 'position': [], 'j_mouv': [], 'loose': True,
           'a_mouv': [False] * 9, 'game': True, 'carte': '',
           'stickers': 3, 'ronds': [], 'sortie': False, 'again': True}
    numero_carte = ''
    # menu
    fltk.cree_fenetre(700, 500)
    fltk.image(350, 250, IMAGE, ancrage='center')
    fltk.texte(280, 200,
               'Veuillez cliqué \n pour voir les differente carte',
               ancrage='center', taille=30)
    fltk.texte(340, 50,
               'Bienvenu dans le labyrinthe !',
               ancrage='center', taille=40)
    
    while jeu['game']:
        jeu['stickers'] = 3
        jeu['ronds']=[]
        jeu['loose'] = True
        # Selection + chargemement carte
        while jeu['again']:
            numero_carte = select_carte()
            if numero_carte == '10':
                tutoriel(jeu)
            elif numero_carte != '':
                restart = afonctions.choix()
                break
        CARTE = cartes.quelle_carte(int(numero_carte), restart)
        jeu['maze'] = fcmaze.ligne_vers_tableau(CARTE)

        while jeu['loose']:
            fltk.efface_tout()
            fltk.image(150, 350, FLECHE, ancrage='nw')
            fltk.texte(580, 0, 'Quitter', couleur='black',
                       ancrage='nw', taille=30)

            if jeu['stickers'] > 0:
                fltk.rectangle(540, 440, 690, 490, epaisseur=3)
                fltk.texte(615, 465, 'STICKER', ancrage='center', taille=25)

            jeu['position'] = fcmaze.position(jeu)
            jeu['a_mouv'] = fcmaze.mouvement_autoriser(jeu)
            fltk.mise_a_jour()
            jeu['a_mouv'] = fcmaze.mouvement_autoriser(jeu)

            while True:
                jeu['sortie'] = True
                afonctions.chemin(jeu)
                afonctions.affiche_stickers(jeu)
                jeu['j_mouv'] = [False] * 4
                click = fltk.attend_clic_gauche()
                if afonctions.sur_bouton(bouton.buttons['devant'], click):
                    jeu['j_mouv'][2] = True
                    jeu['loose'] = fcmaze.mouvement(jeu)
                    break
                elif afonctions.sur_bouton(bouton.buttons['left'], click):
                    jeu['j_mouv'][0] = True
                    jeu['loose'] = fcmaze.mouvement(jeu)
                    break
                elif afonctions.sur_bouton(bouton.buttons['right'], click):
                    jeu['j_mouv'][1] = True
                    jeu['loose'] = fcmaze.mouvement(jeu)
                    break
                elif afonctions.sur_bouton(bouton.buttons['recule'], click):
                    jeu['j_mouv'][3] = True
                    jeu['loose'] = fcmaze.mouvement(jeu)
                    break
                elif afonctions.sur_bouton(bouton.buttons['gauche'], click):
                    jeu['maze'] = fcmaze.turn_to_left(jeu)
                    break
                elif afonctions.sur_bouton(bouton.buttons['droite'], click):
                    jeu['maze'] = fcmaze.turn_to_right(jeu)
                    break
                elif afonctions.sur_bouton(bouton.buttons['quitter'], click):
                    jeu['game'] = False
                    jeu['loose'] = False
                    jeu['sortie'] = False
                    break
                elif jeu['stickers'] > 0 and afonctions.sur_bouton(bouton.buttons['stickers'],
                                                                   click):
                    fcmaze.sticker(jeu)

            if not jeu['loose'] and jeu['sortie']:

                fltk.rectangle(0, 0, 700, 500, remplissage='black')
                fltk.image(350, 250, WIN, ancrage='center')
                fltk.texte(220, 50, 'FELICITATION !', couleur='black',
                           ancrage='nw', taille=30)
                fltk.texte(240, 340, 'Quitter', couleur='black',
                           ancrage='nw', taille=30)
                fltk.texte(240, 250, 'Menu', couleur='black',
                           ancrage='nw', taille=30)
                fltk.texte(240, 160, 'Rejouer', couleur='black',
                           ancrage='nw', taille=30)
                fltk.mise_a_jour()
                CARTE = cartes.quelle_carte(int(numero_carte), True)
                while True:
                    clic = fltk.attend_clic_gauche()
                    if afonctions.sur_bouton(bouton.buttons['play_again'],
                                             clic):
                        jeu['again'] = False
                        break

                    elif afonctions.sur_bouton(bouton.buttons['menu'], clic):
                        jeu['again'] = True
                        break

                    elif afonctions.sur_bouton(bouton.buttons['exit'], clic):
                        jeu['game'] = False
                        break
            fcmaze.maj_maze(jeu, CARTE)
    fltk.attend_ev()
    # fermeture et sortie
    fltk.ferme_fenetre() 