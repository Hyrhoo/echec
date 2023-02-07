# -*- coding: utf-8 -*-
"""
Created on Wed May 11 08:13:57 2022

@author: jojoj
"""

#from random import shuffle
import pygame
pygame.init()
reso = (640,640)
fenetre_de_jeu = pygame.display.set_mode(reso)

place_des_piece = [("to","n",1),("ch","n",1),("fu","n",1),("da","n",1),("ro","n",1),("fu","n",2),("ch","n",2),("to","n",2),
                   ("pi","n",1),("pi","n",2),("pi","n",3),("pi","n",4),("pi","n",5),("pi","n",6),("pi","n",7),("pi","n",8),
                   0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,
                   ("pi","b",1),("pi","b",2),("pi","b",3),("pi","b",4),("pi","b",5),("pi","b",6),("pi","b",7),("pi","b",8),
                   ("to","b",1),("ch","b",1),("fu","b",1),("da","b",1),("ro","b",1),("fu","b",2),("ch","b",2),("to","b",2)]

noir = (100,100,100)
beige = (255,175,175)

#shuffle(place_des_piece)
for i in range(8):
    txt = "["
    for y in range(8):
        txt += str(place_des_piece[y+i*8])+", "
    print(txt+"]")

def affichage():
    fenetre_de_jeu.fill((100,100,100))
    image = pygame.image.load("piece/plateau.png").convert_alpha()
    image_load = pygame.transform.scale(image,(640,640))
    fenetre_de_jeu.blit(image_load,(0,0))
    for y,i in enumerate(place_des_piece):
        if i != 0:
            image = pygame.image.load("piece/"+i[0]+i[1]+".png").convert_alpha()
            image_load = pygame.transform.scale(image,(72,72))
            fenetre_de_jeu.blit(image_load,(32+(y%8)*72,32+(y//8)*72))
    pygame.display.flip()

def deplacement_pion(piece,pos, place_des_piece_test):
    if piece[1] == "n":
        fut_pos = [pos+8 if pos+8 <= 63 and (pos+8)//8 == pos//8+1 and place_des_piece_test[pos+8] == 0 else None,
                   pos+16 if pos+16 <= 63 and (pos+16)//8 == pos//8+2 and pos//8 == 1 and place_des_piece_test[pos+16] == 0 else None,
                   pos+7 if pos+7 <= 63 and (pos+7)//8 == pos//8+1 and (place_des_piece_test[pos+7] != 0 and place_des_piece_test[pos+7][1] == "b") else None,
                   pos+9 if pos+9 <= 63 and (pos+9)//8 == pos//8+1 and (place_des_piece_test[pos+9] != 0 and place_des_piece_test[pos+9][1] == "b") else None]
    elif piece[1] == "b":
        fut_pos = [pos-8 if pos-8 >= 0 and (pos-8)//8 == pos//8-1 and place_des_piece_test[pos-8] == 0 else None,
                   pos-16 if pos-16 >= 0 and (pos-16)//8 == pos//8-2 and pos//8 == 6 and place_des_piece_test[pos-16] == 0 else None,
                   pos-7 if pos-7 >= 0 and (pos-7)//8 == pos//8-1 and (place_des_piece_test[pos-7] != 0 and place_des_piece_test[pos-7][1] == "n") else None,
                   pos-9 if pos-9 >= 0 and (pos-9)//8 == pos//8-1 and (place_des_piece_test[pos-9] != 0 and place_des_piece_test[pos-9][1] == "n") else None]
    return [i for i in fut_pos if i != None]

def deplacement_tour(piece,pos, place_des_piece_test):
    fut_pos = []
    pos2 = pos
    vide = True
    while (pos2+8 <= 63 and (place_des_piece_test[pos2+8] == 0 or (place_des_piece_test[pos2+8][1] == ("b" if piece[1] == "n" else "n")))) and vide:
        pos2 += 8
        if place_des_piece_test[pos2] != 0: vide = False
        fut_pos.append(pos2)
    pos2 = pos
    vide = True
    while (pos2-8 >= 0 and (place_des_piece_test[pos2-8] == 0 or (place_des_piece_test[pos2-8][1] == ("b" if piece[1] == "n" else "n")))) and vide:
        pos2 -= 8
        if place_des_piece_test[pos2] != 0: vide = False
        fut_pos.append(pos2)
    pos2 = pos
    vide = True
    while ((pos2+1)//8 == pos//8 and (place_des_piece_test[pos2+1] == 0 or (place_des_piece_test[pos2+1][1] == ("b" if piece[1] == "n" else "n")))) and vide:
        pos2 += 1
        if place_des_piece_test[pos2] != 0: vide = False
        fut_pos.append(pos2)
    pos2 = pos
    vide = True
    while ((pos2-1)//8 == pos//8 and (place_des_piece_test[pos2-1] == 0 or (place_des_piece_test[pos2-1][1] == ("b" if piece[1] == "n" else "n")))) and vide:
        pos2 -= 1
        if place_des_piece_test[pos2] != 0: vide = False
        fut_pos.append(pos2)
    return fut_pos

def deplacement_foue(piece,pos, place_des_piece_test):
    fut_pos = []
    pos2 = pos
    vide = True
    while ((pos2+9 <= 63 and (pos2+9)%8 > pos%8) and (place_des_piece_test[pos2+9] == 0 or (place_des_piece_test[pos2+9][1] == ("b" if piece[1] == "n" else "n")))) and vide:
        pos2 += 9
        if place_des_piece_test[pos2] != 0: vide = False
        fut_pos.append(pos2)
    pos2 = pos
    vide = True
    while ((pos2+7 <= 63 and (pos2+7)%8 < pos%8) and (place_des_piece_test[pos2+7] == 0 or (place_des_piece_test[pos2+7][1] == ("b" if piece[1] == "n" else "n")))) and vide:
        pos2 += 7
        if place_des_piece_test[pos2] != 0: vide = False
        fut_pos.append(pos2)
    pos2 = pos
    vide = True
    while ((pos2-7 >= 0 and (pos2-7)%8 > pos%8) and (place_des_piece_test[pos2-7] == 0 or (place_des_piece_test[pos2-7][1] == ("b" if piece[1] == "n" else "n")))) and vide:
        pos2 -= 7
        if place_des_piece_test[pos2] != 0: vide = False
        fut_pos.append(pos2)
    pos2 = pos
    vide = True
    while ((pos2-9 >= 0 and (pos2-9)%8 < pos%8) and (place_des_piece_test[pos2-9] == 0 or (place_des_piece_test[pos2-9][1] == ("b" if piece[1] == "n" else "n")))) and vide:
        pos2 -= 9
        if place_des_piece_test[pos2] != 0: vide = False
        fut_pos.append(pos2)
    return fut_pos

def deplacement_chavalier(piece, pos, place_des_piece_test):
    fut_pos = [pos+17 if pos+17 <= 63 and (place_des_piece_test[pos+17] == 0 or place_des_piece_test[pos+17][1] == ("n" if piece[1] == "b" else "b")) and (pos+17)//8 == pos//8+2 else None,
               pos+15 if pos+15 <= 63 and (place_des_piece_test[pos+15] == 0 or place_des_piece_test[pos+15][1] == ("n" if piece[1] == "b" else "b")) and (pos+15)//8 == pos//8+2 else None,
               pos+10 if pos+10 <= 63 and (place_des_piece_test[pos+10] == 0 or place_des_piece_test[pos+10][1] == ("n" if piece[1] == "b" else "b")) and (pos+10)//8 == pos//8+1 else None,
               pos+6 if pos+6 <= 63 and (place_des_piece_test[pos+6] == 0 or place_des_piece_test[pos+6][1] == ("n" if piece[1] == "b" else "b")) and (pos+6)//8 == pos//8+1 else None,
               pos-6 if pos-6 >= 0 and (place_des_piece_test[pos-6] == 0 or place_des_piece_test[pos-6][1] == ("n" if piece[1] == "b" else "b")) and (pos-6)//8 == pos//8-1 else None,
               pos-10 if pos-10 >= 0 and (place_des_piece_test[pos-10] == 0 or place_des_piece_test[pos-10][1] == ("n" if piece[1] == "b" else "b")) and (pos-10)//8 == pos//8-1 else None,
               pos-15 if pos-15 >= 0 and (place_des_piece_test[pos-15] == 0 or place_des_piece_test[pos-15][1] == ("n" if piece[1] == "b" else "b")) and (pos-15)//8 == pos//8-2 else None,
               pos-17 if pos-17 >= 0 and (place_des_piece_test[pos-17] == 0 or place_des_piece_test[pos-17][1] == ("n" if piece[1] == "b" else "b")) and (pos-17)//8 == pos//8-2 else None]
    return [i for i in fut_pos if i != None]

def deplacement_roi(piece, pos, place_des_piece_test):
    fut_pos = [pos+9 if pos+9 <= 63 and (place_des_piece_test[pos+9] == 0 or place_des_piece_test[pos+9][1] == ("n" if piece[1] == "b" else "b")) and (pos+9)//8 == pos//8+1 else None,
               pos+8 if pos+8 <= 63 and (place_des_piece_test[pos+8] == 0 or place_des_piece_test[pos+8][1] == ("n" if piece[1] == "b" else "b")) and (pos+8)//8 == pos//8+1 else None,
               pos+7 if pos+7 <= 63 and (place_des_piece_test[pos+7] == 0 or place_des_piece_test[pos+7][1] == ("n" if piece[1] == "b" else "b")) and (pos+7)//8 == pos//8+1 else None,
               pos+1 if pos+1 <= 63 and (place_des_piece_test[pos+1] == 0 or place_des_piece_test[pos+1][1] == ("n" if piece[1] == "b" else "b")) and (pos+1)//8 == pos//8 else None,
               pos-1 if pos-1 >= 0 and (place_des_piece_test[pos-1] == 0 or place_des_piece_test[pos-1][1] == ("n" if piece[1] == "b" else "b")) and (pos-1)//8 == pos//8 else None,
               pos-7 if pos-7 >= 0 and (place_des_piece_test[pos-7] == 0 or place_des_piece_test[pos-7][1] == ("n" if piece[1] == "b" else "b")) and (pos-7)//8 == pos//8-1 else None,
               pos-8 if pos-8 >= 0 and (place_des_piece_test[pos-8] == 0 or place_des_piece_test[pos-8][1] == ("n" if piece[1] == "b" else "b")) and (pos-8)//8 == pos//8-1 else None,
               pos-9 if pos-9 >= 0 and (place_des_piece_test[pos-9] == 0 or place_des_piece_test[pos-9][1] == ("n" if piece[1] == "b" else "b")) and (pos-9)//8 == pos//8-1 else None]
    return [i for i in fut_pos if i != None]

def deplacement_dame(piece, pos, place_des_piece_test):
    fut_pos = deplacement_tour(piece, pos, place_des_piece_test)
    for i in deplacement_foue(piece, pos, place_des_piece_test):
        fut_pos.append(i)
    return fut_pos

dico_fonction_dep = {"pi": deplacement_pion,
                     "to": deplacement_tour,
                     "fu": deplacement_foue,
                     "ch": deplacement_chavalier,
                     "ro": deplacement_roi,
                     "da": deplacement_dame}

def deplacement(piece, pos, place_des_piece_test):
    #print(pos//8,pos%8, pos)
    #for i in range(8):
    #    txt = "["
    #    for y in range(8):
    #        txt += str(place_des_piece_test[y+i*8])+", "
    #    print(txt+"]")
    return dico_fonction_dep[piece[0]](piece, pos, place_des_piece_test)

def afficher_deplacement(poss, coul = (100,100,255)):
    for i in poss:
        #print(i)
        y = i//8
        x = i%8
        #print(x,y)
        rectangle = pygame.Rect(32+(72*x), 32+(72*y), 72, 72)
        pygame.draw.rect(fenetre_de_jeu, coul, rectangle, 10, 20)
    pygame.display.flip()

def verif_defaite(piece, pos, place_des_piece):
    coup_pos = deplacement_roi(piece, pos, place_des_piece)
    pas_bon = []
    #print("")
    #print(pos, "pos ini")
    for z,i in enumerate(coup_pos):
        place_des_piece_2 = place_des_piece.copy()
        place_des_piece_2[pos] = 0
        place_des_piece_2[i] = piece
        #print("")
        #print(i, "nouv pos")
        for x,y in enumerate(place_des_piece_2):
            if y != 0 and y[1] != piece[1]:
                #print(x, "pos piece attaque")
                mov_en = deplacement(y,x, place_des_piece_2)
                #print(mov_en)
                if i in mov_en:
                    pas_bon.append(i)
                    break
    coup_pos = [i for i in coup_pos if i not in pas_bon]
    continu = bool(len(coup_pos))
    return continu, coup_pos

def verif_echec(coul):
    for i,y in enumerate(place_des_piece):
        if y == ("ro",coul,1):
            pos = i
            print(pos)
    for y,i in enumerate(place_des_piece):
        if i != 0 and i[1] != coul:
            if pos in dico_fonction_dep[i[0]](i, y, place_des_piece):
                return True, pos
    return False, None

def select_ou_dep(piece, pos, piece_select, pos_select, coul, dep):
    if piece == piece_select:
        return False, None, None, True
    if not piece and piece_select[1] == coul and piece_select[0] == "pi":
        if (coul == "n" and pos_select in range(55,64)) or (coul == "b" and pos_select in range(0,8)):
            rectangle = pygame.Rect(200, 200, 240, 240)
            pygame.draw.rect(fenetre_de_jeu, (100,100,100), rectangle, 0, 20)
            t_piece = ("to","fu","ch","da")
            for j,i in enumerate(t_piece):
                image = pygame.image.load("piece/"+i+coul+".png").convert_alpha()
                image_load = pygame.transform.scale(image,(100,100))
                fenetre_de_jeu.blit(image_load,(220+(j//2)*100,220+(j%2)*100))
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        ps = event.pos
                        if ps[0] in range(220, 420) and ps[1] in range(220, 420):
                            num_piece = (2*(ps[0]-220)//100)+((ps[1]-220)//100)
                            place_des_piece[pos_select] = (t_piece[num_piece], coul, 1)
                            return True, None, None, True
                        return False, None, None, True
    if not piece and piece_select[1] == coul:
        return False, piece_select, pos_select, True
    if piece and pos is not None and dep:
        if pos_select in dep:
            place_des_piece[pos] = 0
            place_des_piece[pos_select] = piece
            return True, None, None, True
    return False, piece, pos, False

def invers_coul(coul):
    if coul == "n":
        return "b"
    if coul == "b":
        return "n"

piece = ("ro","b",1)
for i,y in enumerate(place_des_piece):
    #print(y, piece, y==piece)
    if y == piece: pos = i

affichage()
clock = pygame.time.Clock()
coul = "n"
lencer = True
partie = True
suite = True
while lencer:
    if suite:
        affichage()
        coul = invers_coul(coul)
        print("tour des "+("noirs" if coul == "n" else "blancs"))
        piece = None # pas desois d'initialiser pos car si le roi n'es pas en echec,
                     # la fonctin verif_echec renvois (False, None) donc initialise pos a None
        echec, pos = verif_echec(coul)
        print(echec)
        if echec:
            coup_roi = verif_defaite(("ro",coul,1), pos, place_des_piece)
            if len(coup_roi) == 0:
                print("echec et mat")
                partie = False
            else:
                print("roi "+("noir" if coul == "n" else "blanc")+" en echec")
                piece = ("ro",coul,1)
                y = pos//8
                x = pos%8
                #print(x,y)
                rectangle = pygame.Rect(32+(72*x), 32+(72*y), 72, 72)
                pygame.draw.rect(fenetre_de_jeu, (255,100,100), rectangle, 10, 20)
                pygame.display.flip()
    suite = False
    dep = None
    if pos is not None and piece:
        dep = deplacement(piece, pos, place_des_piece)
        if piece[0] == "ro": _, dep = verif_defaite(piece, pos, place_des_piece)
        if not echec:
            y = pos//8
            x = pos%8
            rectangle = pygame.Rect(32+(72*x), 32+(72*y), 72, 72)
            pygame.draw.rect(fenetre_de_jeu, (100,255,100), rectangle, 10, 20)
        afficher_deplacement(dep)
    if pos is None and not piece:
        affichage()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lencer = False
        valide = False
        if event.type == pygame.MOUSEBUTTONUP and partie and not valide:
            if event.pos[0] in range(32, 608) and event.pos[1] in range(32, 608):
                pos_select = ((event.pos[0]-32)//72)+((event.pos[1]-32)//72)*8
                piece_select = place_des_piece[pos_select] 
                print(piece_select, pos_select)
                if piece_select != 0 or piece:
                    suite, piece, pos, valide = select_ou_dep(piece, pos, piece_select, pos_select, coul, dep)
    clock.tick(60)

pygame.quit()
