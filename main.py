import pygame
from pygame.locals import QUIT, RESIZABLE
import time

pygame.font.init()
font1 = pygame.font.Font(None, 25)
font = pygame.font.SysFont("arial",50)
font2 = pygame.font.SysFont("comic_sans_ms",20)
black = (0,0,0)

x= 1180
y=600

import random
import json

class Joueur:
    def __init__(self, nom):
        self.case = 0
        self.nom = nom
        self.points = 0
        self.pieces = 7
        self.objets = []
        self.pieces_repas = 0
        self.rencontres = 0
        self.personnage = None
        self.sources_chaudes = 0
        self.paysages_riz = 0
        self.paysages_montagne= 0
        self.paysages_mer = 0
        self.pieces_temple = 0
        self.repas_manges = []

    def __str__ (self):
        return f"{self.nom} : {self.points} pts, {self.pieces} pièces"
        
    def acheter_objet(self, objet):
        if self.pieces >= objet.prix:
            self.pieces -= objet.prix
            self.points += objet.prix+1
            self.objets.append(objet)
            print("Objet acheté avec succès!")
        else:
            print("Vous n'avez pas assez d'argent.")

    def acheter_repas(self, repas):
        if self.pieces >= repas.prix:
            self.pieces -= repas.prix
            self.pieces_repas += repas.prix
            self.repas_manges.append(repas)
            self.points += 6
            print("Repas acheté avec succès!")
        else:
            print("Vous n'avez pas assez d'argent.")
        
    def ajouter_points(self, points):
        self.points += points
        
    def ajouter_pieces(self, pieces):
        self.pieces += pieces
    
    def avancer(self,avancement):
        self.case = self.case + avancement

class Objet:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
    def __str__ (self):
        return f"Souvenir : {self.nom}, Prix : {self.prix}"

class Repas :
    def __init__ (self, nom, prix) :
        self.prix = prix
        self.nom = nom
    
    def __str__ (self):
        return f"Repas : {self.nom}, Prix : {self.prix}"

liste_objets = [Objet("Koma", 1), Objet("Gofu",1), Objet("Washi",1), Objet("Hashi",1), Objet("Uchiwa",1), Objet("Yunomi",1), Objet("Ocha", 2), Objet("Sake", 2), Objet("Konpemo", 1), Objet("Kamaboko", 1,), Objet("Daifuku", 2), Objet("Manvu", 1), Objet("Netsuke", 2), Objet("Shamisen", 3), Objet("Vubako", 2), Objet("Sume", 3), Objet("Shiki", 2), Objet("Ukiyoe", 3), Objet("Kanzashi",2), Objet("Sandogasa",2), Objet("Geta",2), Objet("Haori",2), Objet("Yukata",2), Objet("Furoshiki",2)]
Tai_meshi=Repas("Tai_meshi",3)
Udon =Repas("Udon", 3)
Unago =Repas ("Unagi", 3)
Tempura = Repas("Tempura",2)
Soba = Repas("Soba", 2)
Misoshiru = Repas("Misoshiru", 1)
Tofu = Repas("Tofu", 2)
Sushi = Repas("Sushi", 2)
Dango = Repas("Dango", 1)
Donburi = Repas("Donburi", 3)
Fugu = Repas ("Fugu", 3)
Sashimi = Repas("Sashimi", 3)
Yakitori = Repas("Yakitori", 2)
Nigirimeshi = Repas("Nigirimeshi",1)
liste_repas= [Tai_meshi, Udon, Unago, Tempura, Soba, Misoshiru, Tofu, Sushi, Dango, Donburi, Fugu, Sashimi, Yakitori, Nigirimeshi]

class Temple:

    def __init__(self,liste_joueurs) :
        self.caisse = {}
        for joueur in liste_joueurs :
            self.caisse[joueur] = 0

    def don1 (self, joueur):
        if joueur.pieces ==0:
            message_box.text = "Vous êtes trop pauvres pour donner au temple"
            message_box.text2 = ""
            message_box.text3 = ""
            message_box.text4 = ""
        else : 
            message_box.text = "Combien voulez-vous donner de pièces au temple (1 à 3) "
            message_box.text2 = ""
            message_box.text3 = ""
            message_box.text4 = ""
    
    def don2(self,joueur,dons) :
            if joueur.pieces >= dons :    
                joueur.ajouter_pieces(-dons)    
                self.caisse[joueur]=self.caisse[joueur]+dons
                joueur.ajouter_points(dons)
                message_box.text = "Votre don a bien été reçu"
                message_box.text2 = ""
                message_box.text3 = ""
                message_box.text4 = ""
            else :
                message_box.text = "Vous n'avez pas autant argent à donner D:"
                message_box.text2 = ""
                message_box.text3 = ""
                message_box.text4 = ""
    def don_banque (self, joueur):
        message_box.text2 = "La prêtresse a mis une pièce au temple pour vous ! "
        message_box.text = ""
        message_box.text3 = ""
        message_box.text4 = ""
        self.caisse[joueur]=self.caisse[joueur]+1
        joueur.ajouter_points(1)
liste_joueurs = []

class Rencontre:
    def __init__(self, nom, effet):
        self.nom = nom
        self.effet = effet
    
    def __str__ (self):
        return f"Vous faites la rencontre de {self.nom} ! "
       
    def appliquer_effet(self, joueur):
        if self.effet == "piece pour le temple":
            Temple(liste_joueurs).don_banque(joueur)
        elif self.effet == "points":
            joueur.ajouter_points(3)
            message_box.text2 = "Vous gagnez 3 points grâce à cette rencontre"
            
        elif self.effet == "pieces":
            n=random.choice([1,2,3])
            joueur.ajouter_pieces(n)
            message_box.text2 = "Vous gagnez "+str(n)+" pièces grâce à cette rencontre"
            
        elif self.effet == "objet":
            num_objet = random.randrange(0,len(liste_objets),1)
            joueur.objets.append(liste_objets[num_objet])
            message_box.text2 = "Vous avez obtenu l'objet : "+ liste_objets[num_objet].nom
            
            del(liste_objets[num_objet])
        elif self.effet == "paysage_riz":
            if joueur.paysages_riz < 3 :
                message_box.text2 = "Vous avez reçu une carte paysage de rizière ! "
                joueur.ajouter_points(joueur.paysages_riz+1)
                joueur.paysages_riz += 1
            else : 
                
                if joueur.paysages_montagne <4 :
                    message_box.text2 = "Vous avez reçu une carte paysage de montagne car vous aviez déjà toutes celles de rizière ! "
                    joueur.ajouter_points(joueur.paysages_montagne+1)
                    joueur.paysages_montagne += 1 
                else :
                    if joueur.paysages_mer < 5 :
                        message_box.text2 = "Vous avez reçu une carte paysage de mer car vous aviez déjà toutes celles de rizière ! "
                        joueur.ajouter_points(joueur.paysages_mer+1)
                        joueur.paysages_mer += 1
                    else :
                        message_box.text2 = "Vous avez déjà toutes les cartes paysages ! "
                    
        elif self.effet == "paysage_montagne":
            if joueur.paysages_montagne <4 :
                message_box.text2 = "Vous avez reçu une carte paysage de montagne ! "
                joueur.ajouter_points(joueur.paysages_montagne+1)
                joueur.paysages_montagne += 1
            else : 
                    if joueur.paysages_riz < 3 :
                        message_box.text2 = "Vous avez reçu une carte paysage de rizière car vous aviez déjà toutes celles de montagne ! "
                        joueur.ajouter_points(joueur.paysages_riz+1)
                        joueur.paysages_riz += 1
                    else :
                        if joueur.paysages_mer < 5 :
                            message_box.text2 = "Vous avez reçu une carte paysage de mer car vous aviez déjà toutes celles de montagne ! "
                            joueur.ajouter_points(joueur.paysages_mer+1)
                            joueur.paysages_mer += 1
                        else :
                            message_box.text2 = "Vous avez déjà toutes les cartes paysages ! "
        elif self.effet == "paysage_mer":
            if joueur.paysages_mer < 5 :
                message_box.text2 = "Vous avez reçu une carte paysage de mer ! "
                joueur.ajouter_points(joueur.paysages_mer+1)
                joueur.paysages_mer += 1
                
            else : 
                    if joueur.paysages_montagne <4 :
                        message_box.text2 = "Vous avez reçu une carte paysage de mer car vous aviez déjà toutes celles de rizière ! "
                        joueur.ajouter_points(joueur.paysages_montagne+1)
                        joueur.paysages_montagne += 1
                        
                    else :
                        if joueur.paysages_riz < 3 :
                            message_box.text2 = "Vous avez reçu une carte paysage de mer car vous aviez déjà toutes celles de rizière ! "
                            joueur.ajouter_points(joueur.paysages_riz+1)
                            joueur.paysages_riz += 1
                        else :
                            message_box.text2 = "Vous avez déjà toutes les cartes paysages ! "      

liste_rencontres = [Rencontre("Miko", "piece pour le temple"),Rencontre("Miko ", "piece pour le temple"),
Rencontre("Kuge", "pieces"),Rencontre("Kuge ", "pieces"),Rencontre("Shokunin ","objet"), 
Rencontre("Shokunin","objet"), Rencontre("Samurai","points"),Rencontre("Samurai ","points"),
Rencontre("Annaibito", "paysage_riz"),Rencontre("Annaibito ", "paysage_riz"),Rencontre("Annaibito", "paysage_montagne"),
Rencontre("Annaibito ", "paysage_montagne"),Rencontre("Annaibito", "paysage_mer"), Rencontre("Annaibito ", "paysage_mer")]

def rencontre(joueur):
    choix_rencontre = random.randint(0,len(liste_rencontres))
    perso_rencontre = liste_rencontres[choix_rencontre]
    del(liste_rencontres[choix_rencontre])
    perso_rencontre.appliquer_effet(joueur)
    return perso_rencontre

def Echoppe1 ( liste_objets):

    choix1 = random.randint(0,len(liste_objets))
    objet_1 = liste_objets[choix1]
    del(liste_objets[choix1])

    choix2 = random.randint(0,len(liste_objets))
    objet_2 = liste_objets[choix2]
    del(liste_objets[choix2])

    choix3 = random.randint(0,len(liste_objets))
    objet_3 = liste_objets[choix3]
    del(liste_objets[choix3])

    objets_achetables = { "objet_1":objet_1, "objet_2": objet_2, "objet_3":objet_3}
    
    message_box.text = "Bienvenue à l'échoppe, voici les souvenirs achetables :"
    message_box.text2 = str(objet_1)+" / "+str(objet_2)+" / "+str(objet_3)
    
    message_box.text3="Quel(s) souvenir(s) voulez vous acheter parmi ceux-ci ? Mettez un espace entre les numéros"
    message_box.text4=" des souvenirs si vous en achetez plusieurs. Ex: 1 3 pour acheter les numéros 1 et 3"
    

    return objets_achetables

def acheter (joueur, achete,objets_achetables):
    if achete == 1 :
        joueur.acheter_objet(objets_achetables["objet_1"])
        message_box.text2 = "Votre souvenir a bien été acheté"
        del(objets_achetables["objet_1"])
    if achete == 2 :
        joueur.acheter_objet(objets_achetables["objet_2"])
        message_box.text3 = "Votre souvenir a bien été acheté"
        del(objets_achetables["objet_2"])
    if achete == 3 :
        joueur.acheter_objet(objets_achetables["objet_3"])
        message_box.text4 = "Votre souvenir a bien été acheté"
        del(objets_achetables["objet_3"])
    

def Echoppe2(joueur,objets_achetables,achats):
    message_box.text = ""
    message_box.text2 = ""
    message_box.text3 = ""
    message_box.text4 = ""
    if len(achats) == 1 :
        achete1 = int(achats)
        acheter(joueur,achete1,objets_achetables)
    
    if len(achats)==3 :
        achete1=int(achats[0])
        acheter(joueur,achete1,objets_achetables)
        achete2 = int(achats[2])
        acheter(joueur,achete2,objets_achetables)
        
    if len(achats)==5:
        achete1=int(achats[0])
        acheter(joueur,achete1,objets_achetables)
        achete2 = int(achats[2])
        acheter(joueur,achete2,objets_achetables)
        achete3 = int(achats[4])
        acheter(joueur,achete3,objets_achetables)
        
    for cle in objets_achetables :
        liste_objets.append(objets_achetables[cle])
    
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = black
        self.text = text
        self.font = pygame.font.Font(None, 25)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si l'utilisateur clique sur la boîte de saisie, elle devient active
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            # La couleur de la boîte de saisie change en fonction de son état
            self.color = "grey" if self.active else black
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # Si l'utilisateur appuie sur Entrée, le texte est enregistré
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    # Si l'utilisateur appuie sur la touche Backspace, le texte est effacé
                    self.text = self.text[:-1]
                else:
                    # Ajout des caractères saisis à la fin du texte
                    self.text += event.unicode
                # La surface de texte est mise à jour pour refléter les changements
                self.txt_surface = self.font.render(self.text, True, "black")

input_box1 = InputBox(480, 215, 200, 32)
input_box2 = InputBox(480, 300, 200, 32)
input_box_jeu = InputBox(115, 490, 100, 32)
input_box_nb_joueurs = InputBox(580, 20, 80, 32)

class MessageBox:

    def __init__(self, x, y, w, h, text='',text2='',text3='',text4=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = black
        self.text = text
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4
        self.font = pygame.font.Font(None, 25)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def draw(self, screen):
        self.txt_surface = self.font.render(self.text, True, "black")
        self.txt2_surface = self.font.render(self.text2, True, "black")
        self.txt3_surface = self.font.render(self.text3, True, "black")
        self.txt4_surface = self.font.render(self.text4, True, "black")
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x + 7, self.rect.y + 5))
        screen.blit(self.txt2_surface, (self.rect.x + 7, self.rect.y + 25))
        screen.blit(self.txt3_surface, (self.rect.x + 7, self.rect.y + 45))
        screen.blit(self.txt4_surface, (self.rect.x + 7, self.rect.y + 65))
    
message_box = MessageBox(385,480,775,100)

class Bouton:

    def __init__(self, x, y, w, h, text,screen):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = black
        self.text = text
        self.font = pygame.font.Font(None, 25)
        self.txt_surface = self.font.render(text, True, self.color)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))       
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si l'utilisateur clique sur la boîte de saisie, elle devient active
            if self.rect.collidepoint(event.pos):
                self.active = True

use_screen = "accueil"

database = {}

try:
    with open("database.json", "r") as f:
        database = json.load(f)
except FileNotFoundError:
    pass

def save_database():
    with open("database.json", "w") as f:
        json.dump(database, f)

# Fonction pour créer un nouveau compte utilisateur
def create_account(pseudo,password):
    
    if pseudo in database:
        print("Le nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
        return False
    else :
        database[pseudo] = {"password": password, "victoires": 0, "defaites": 0}
        save_database()
        print("Compte créé avec succès.")
        return True

# Fonction pour connecter un utilisateur existant
def login(pseudo,password):
    
    if pseudo in database:
        if password == database[pseudo]["password"]:
            print("Connexion réussie.")
            return True
           
        else:
            print("Mot de passe incorrect.")
            return False
    else:
        print("Nom d'utilisateur inconnu.")
        return False
    
liste_joueurs = []

#création de la classe Gmae qui va gérer tout ce qui se passe à l'écran
class Game: 
    def __init__ (self,screen,x,y):
        self.screen = screen
        self.running = True 
        self.longueur = x
        self.largeur = y
        self.joueurs_co = 1
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0
        self.r4 = 0
        self.cases_des_joueurs=[]
        self.joueurs_finis = []
        self.state = "avancer"
        self.t = 0

    def run(self,use_screen):
        while self.running :
            if use_screen == "accueil":
                screen.fill((255,255,255))
                screen.blit(fond, fond.get_rect(center = (self.longueur/2, self.largeur/2.8)))
                screen.blit(Bouton_play, Bouton_play.get_rect(center = (self.longueur/2, self.largeur*0.80-25) ))
                screen.blit(Bouton_exit, Bouton_exit.get_rect(center = (self.longueur/2, self.largeur*0.80+70) ))
                bouton_regles.draw(screen)
                bouton_scores.draw(screen)
                pygame.display.flip()
            
                
                while self.running and use_screen=="accueil" :
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT :
                            self.running = False   
                        if event.type == pygame.MOUSEBUTTONDOWN :
                            pos = pygame.mouse.get_pos()
                            if self.longueur/2-75 <= pos[0] <= self.longueur/2+75 and self.largeur*0.80+30 <= pos[1] <= self.largeur*0.80+110 :
                                self.running = False
                            if self.longueur/2-75 <= pos[0] <= self.longueur/2+75 and self.largeur*0.80-65 <= pos[1] <= self.largeur*0.80+15 :
                                use_screen = "nb_joueurs"
                            if bouton_regles.rect.collidepoint(event.pos):
                                use_screen = "regles"
                            if bouton_scores.rect.collidepoint(event.pos):
                                use_screen = "scores"
                                
            if use_screen == "scores":
                screen.fill((255,255,255))
                bouton_retour.draw(screen) 
                nb_comptes = 0         
                for cle in database :
                    resultat = cle
                    resultat1 = database[cle]["victoires"]
                    resultat2 = database[cle]["defaites"]
                    nb_comptes += 1
                    print(resultat, resultat1, resultat2)
                font1 = pygame.font.Font(None, 50)
                screen.blit(font1.render("Tableau des scores", True, "black"),(400, 20))
                largeur = 100
                longueur = 48    
                font1 = pygame.font.Font(None, 25)
                i = 0
                for cle in database :
                    compteur = 0
                    ecrire = cle
                    
                    for j in range(3):
                        if ecrire == cle and compteur == 0 :
                            compteur = 1
                        elif compteur == 1 :
                            ecrire = database[cle]["victoires"]
                            compteur = 0
                        elif ecrire == database[cle]["victoires"] :
                            ecrire = database[cle]["defaites"]
                        rect = pygame.Rect(j * largeur+400, i * longueur+150, largeur, longueur)
                        screen.blit(font1.render(str(ecrire), True, "black"),(j * largeur+410, i * longueur+160))
                        pygame.draw.rect(screen, "black", rect, 1)
                    i+=1
                            
                
                pygame.display.flip()
      
                while self.running and use_screen=="scores" :
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT :
                            self.running = False   
                        if event.type == pygame.MOUSEBUTTONDOWN :
                            if bouton_retour.rect.collidepoint(event.pos):
                                use_screen = "accueil"    
                                
            if use_screen == "regles":
                screen.fill((255,255,255))
                bouton_retour.draw(screen)
                font = pygame.font.SysFont("arial",50)
                link_text = font.render("Cliquez ici pour consulter les règles de Tokaido !", True, black)
                link_rect = link_text.get_rect()
                link_rect.x = 100
                link_rect.y = 200
                screen.blit(link_text, (100, 200))
                pygame.display.flip()
                
                while self.running and use_screen=="regles" :
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT :
                            self.running = False   
                        if event.type == pygame.MOUSEBUTTONDOWN :
                            if bouton_retour.rect.collidepoint(event.pos):
                                use_screen = "accueil"
                            if link_rect.collidepoint(pygame.mouse.get_pos()):
                                import webbrowser
                                webbrowser.open("https://drive.google.com/file/d/1SzU1_vcR2V23EHsqn_QcCPzDdjS7kpz_/view?usp=drivesdk")
                                
            if use_screen == "nb_joueurs" :
                screen.fill((255,255,255))
                font = pygame.font.SysFont("arial",30)
                text4 = font.render("Nombre de joueurs (3 à 5) :  ", True, "black")
                screen.blit(fond_co, fond_co.get_rect(center = (self.longueur/2, self.largeur/2)))
                screen.blit(text4, (260, 15))
                bouton_valider2.draw(screen)
                bouton_retour.draw(screen)
                input_box_nb_joueurs.draw(screen)
                pygame.display.flip()
                
                input_box_nb_joueurs.draw(screen)
                                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT :
                        self.running = False                    
                    if event.type == pygame.MOUSEBUTTONDOWN :
                        if bouton_retour.rect.collidepoint(event.pos):
                                use_screen = "accueil"
                        if bouton_valider2.rect.collidepoint(event.pos):
                            nb_joueurs = int(input_box_nb_joueurs.text)                
                            use_screen = "choix"              

                    input_box_nb_joueurs.handle_event(event)
                    if event.type == pygame.KEYDOWN:
                        input_box_nb_joueurs.draw(screen)
                
                                            
                pygame.display.flip()    
                
            if use_screen == "choix":
                screen.blit(fond_co, fond_co.get_rect(center = (self.longueur/2, self.largeur/2)))
                font = pygame.font.SysFont("arial",30)
                text6 = font.render("Joueur "+str(self.joueurs_co), True, "black")
                screen.blit(text6, (200, 10))
                bouton_connexion.draw(screen)
                
                bouton_inscription.draw(screen)
                pygame.display.flip()    
                    
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT :
                        self.running = False                    
                    if event.type == pygame.MOUSEBUTTONDOWN :
                        if bouton_connexion.rect.collidepoint(event.pos):
                            use_screen ="connexion"
                        if bouton_inscription.rect.collidepoint(event.pos):
                            use_screen = "inscription"
                

            if use_screen == "connexion":
                                                           
                font = pygame.font.SysFont("arial",50)
                font1 = pygame.font.Font(None, 25)
                font2 = pygame.font.Font(None, 16)
                screen.fill((255,255,255))
                screen.blit(fond_co, fond_co.get_rect(center = (self.longueur/2, self.largeur/2)))       
                text1 = font.render("Connexion", True, "black")
                text2 = font1.render("Identifiant :  ", True, black)
                text3 = font1.render("Mot de Passe :  ", True, black)
                text_refus = font2.render("Si rien ne se passe après avoir cliqué sur le bouton valider, vous vous êtes trompés sur l'indentifiant ", True, "black")
                text_refus2 = font2.render("ou le mot de passe ou alors que le compte n'existe pas donc il faut le créer via l'inscription ", True, "black")
                pygame.draw.rect(screen, "white", pygame.Rect(470, 180, 230, 220))
                pygame.draw.rect(screen, "black", pygame.Rect(470, 180, 230, 220), 2)
                bouton_valider.draw(screen)
                bouton_retour.draw(screen)
                screen.blit(text1, (480, 10))
                screen.blit(text2, (480, 190))
                screen.blit(text3, (480, 270))
                screen.blit(text_refus, (350, y-30))
                screen.blit(text_refus2, (370, y-20))
                input_box1.draw(screen)
                input_box2.draw(screen)
                
                pygame.display.flip()
                               
                input_box1.draw(screen)
                input_box2.draw(screen)
                
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT :
                        self.running = False   
                    if event.type == pygame.MOUSEBUTTONDOWN :
                        if bouton_retour.rect.collidepoint(event.pos):
                                use_screen = "choix"
                        if bouton_valider.rect.collidepoint(event.pos): 
                            if login(input_box1.text,input_box2.text) == True :
                                connexionn = True
                                liste_joueurs.append(Joueur(input_box1.text))
                                input_box1.text = "" 
                                input_box2.text = "" 
                            else :
                                connexionn = False
                            
                            if self.joueurs_co == nb_joueurs and connexionn == True:
                                use_screen = "jeu"
                            elif connexionn == True : 
                                use_screen ="choix"
                                self.joueurs_co += 1                                           
                    
                    input_box1.handle_event(event)
                    input_box2.handle_event(event)

                    if event.type == pygame.KEYDOWN:
                        input_box1.draw(screen)
                        input_box2.draw(screen)
                pygame.display.flip() 
                    
                
                                
            if use_screen == "inscription"  :
                
                font = pygame.font.SysFont("arial",50)
                screen.fill((255,255,255))
                font2 = pygame.font.Font(None, 16)
                
                screen.blit(fond_co, fond_co.get_rect(center = (self.longueur/2, self.largeur/2)))       
                text1 = font.render("Inscription", True, "black")
                text2 = font1.render("Identifiant :  ", True, black)
                text3 = font1.render("Mot de Passe :  ", True, black) 
                text_refus = font2.render("Si rien ne se passe après avoir cliqué sur le bouton valider, cela veut dire   ", True, "black")
                text_refus2 = font2.render("que cet identifiant est déjà pris, veuillez donc en choisir un autre. ", True, "black")
                pygame.draw.rect(screen, "white", pygame.Rect(470, 180, 230, 220))
                pygame.draw.rect(screen, "black", pygame.Rect(470, 180, 230, 220), 2)
                bouton_valider.draw(screen)
                bouton_retour.draw(screen)
                screen.blit(text1, (480, 10))
                screen.blit(text2, (480, 190))
                screen.blit(text3, (480, 270))
                screen.blit(text_refus, (400, y-30))
                screen.blit(text_refus2, (420, y-20))
                input_box1.draw(screen)
                input_box2.draw(screen)
                pygame.display.flip()
                
                
                
                input_box1.draw(screen)
                input_box2.draw(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT :
                        self.running = False                  
                    if event.type == pygame.MOUSEBUTTONDOWN :
                        if bouton_retour.rect.collidepoint(event.pos):
                                use_screen = "choix"
                        if bouton_valider.rect.collidepoint(event.pos): 
                            if create_account(input_box1.text,input_box2.text) == True :
                                inscription = True
                                liste_joueurs.append(Joueur(input_box1.text))
                                input_box1.text = "" 
                                input_box2.text = "" 
                            else :
                                inscription = False
                            
                            pygame.display.update()
                            if self.joueurs_co == nb_joueurs and inscription == True:
                                use_screen = "jeu"
                            elif inscription == True : 
                                use_screen ="choix"
                                self.joueurs_co += 1                            
                    
                    input_box1.handle_event(event)
                    input_box2.handle_event(event)
                    if event.type == pygame.KEYDOWN:
                        input_box1.draw(screen)
                        input_box2.draw(screen)
                pygame.display.flip()          
                            

            if use_screen == "jeu":
                
                cases = ["echoppe","temple","rencontre","paysage_riz","source_chaude","paysage_montagne","ferme","echoppe","temple","rencontre","paysage_mer","paysage_montagne", "source_chaude",
                "relais","paysage_mer","temple","ferme","paysage_riz","paysage_montagne","rencontre","temple","source_chaude","paysage_montagne","paysage_mer","echoppe","ferme","relais", 
                "paysage_riz", "echoppe", "rencontre", "ferme", "paysage_montagne", "source_chaude", "paysage_mer", "paysage_riz", "temple","ferme", "rencontre", "paysage_mer", "echoppe", "relais", 
                "source_chaude", "temple", "rencontre", "echoppe", "paysage_mer", "ferme", "source_chaude", "rencontre", "paysage_montagne","paysage_riz", "paysage_mer", "echoppe", "relais" ]
                
                if self.t== 0 :
                    self.temple = Temple(liste_joueurs)
                    self.t=1

                def repas_relais_1(liste_repas):
                    repas_achetables1 = []

                    for i in range (len(liste_joueurs)+1):
                        choix = random.randint(0,len(liste_repas)-1)
                        repas_achetables1.append(liste_repas[choix]) 
                        self.r1 = 1
                    
                    return repas_achetables1

                if self.r1 == 0 :
                    repas_achetables1=repas_relais_1(liste_repas)


                def repas_relais_2(liste_repas):
                    repas_achetables2 = []

                    for i in range (len(liste_joueurs)+1):
                        choix = random.randint(0,len(liste_repas)-1)
                        repas_achetables2.append(liste_repas[choix])        
                        self.r2 = 1
                    return repas_achetables2

                if self.r2 == 0:
                    repas_achetables2=repas_relais_2(liste_repas)

                def repas_relais_3(liste_repas):
                    repas_achetables3 = []

                    for i in range (len(liste_joueurs)+1):
                        choix = random.randint(0,len(liste_repas)-1)
                        repas_achetables3.append(liste_repas[choix])
                        self.r3 = 1

                    return repas_achetables3

                if self.r3 == 0:
                    repas_achetables3=repas_relais_3(liste_repas)

                def repas_relais_4(liste_repas):
                    repas_achetables4 = []

                    for i in range (len(liste_joueurs)+1):
                        choix = random.randint(0,len(liste_repas)-1)
                        repas_achetables4.append(liste_repas[choix])
                        self.r4 = 1
                        

                if self.r4 == 0:
                    repas_achetables4=repas_relais_4(liste_repas)

                def Relais1(joueur,repas_achetables1,repas_achetables2,repas_achetables3,repas_achetables4):

                    if joueur.case == 14: 
                        repas_achetables = repas_achetables1
                    elif joueur.case == 27 : 
                        repas_achetables = repas_achetables2
                    elif joueur.case == 41 : 
                        repas_achetables = repas_achetables3
                    elif joueur.case ==54  : 
                        repas_achetables = repas_achetables4
                        
                    
                    message_box.text = "Vous êtes arrivé au relais ! Voici les repas achetables :"
                    if len(repas_achetables) < 4 :
                        for i in range (len(repas_achetables)):
                            message_box.text2 += str(repas_achetables[i])+" / "
                    else :
                        for i in range (3):
                            message_box.text2 += str(repas_achetables[i])+" / "
                        for i in range (3,len(repas_achetables)):
                            message_box.text3 += str(repas_achetables[i])+" / "


                    message_box.text4 = "quel repas voulez-vous acheter ( 1 pour le 1er, 2 pour le 2e et 3 pour le 3e etc) "
                    return repas_achetables

                def Relais2 (joueur,repas_achetables1,repas_achetables2,repas_achetables3,repas_achetables4,achete,repas_achetables):
                    if repas_achetables1[achete-1] in joueur.repas_manges :
                        message_box.text4 = "Vous avez déja mangé ce repas" 
                    else:
                        joueur.acheter_repas(repas_achetables[achete-1])
                        del(repas_achetables[achete-1])

                    if joueur.case == 14: 
                        repas_achetables1 = repas_achetables
                    elif joueur.case == 27 : 
                        repas_achetables2 = repas_achetables
                    elif joueur.case == 41 : 
                        repas_achetables3 = repas_achetables
                    elif joueur.case ==54  : 
                        repas_achetables4 = repas_achetables
                        
                def partie_finie():  
                    for joueur in liste_joueurs : 
                        if joueur.case == 54 :
                            if joueur not in self.joueurs_finis :
                                self.joueurs_finis.append(joueur)

                    if len(self.joueurs_finis)==len(liste_joueurs):
                        self.running= False
                
                def Jouer (joueur,avancement):
                    while True : 
                        cases_occupées = []
                        cases_relais = [14,27,41,54]
                        for joueurs in liste_joueurs :
                            cases_occupées.append(joueurs.case)
                        if joueur.case + avancement in cases_occupées  and joueur.case + avancement not in cases_relais :
                            message_box.text = "Cette case est déja occupée par un autre joueur, veuillez en choisir une autre : "
                        else : 
                            joueur.avancer(avancement)
                            case_joueur = cases[joueur.case-1]
                            break
                    
                    if case_joueur == "relais" :
                        self.state = "relais"
                        repas_achetables = Relais1(joueur, repas_achetables1,repas_achetables2,repas_achetables3,repas_achetables4)
                        return repas_achetables
                        

                    if case_joueur== "echoppe":
                        self.state = "echoppe"
                        objets_achetables = Echoppe1(liste_objets)
                        return objets_achetables

                    if case_joueur == "temple":
                        self.state = "temple"
                        self.temple.don1(joueur)
                        
                    if case_joueur == "rencontre":
                        self.state = "rencontre"
                        message_box.text = str(rencontre(joueur))
                        message_box.text3 = ""
                        message_box.text4 = ""
                 
                    if case_joueur == "paysage_riz":
                        self.state = "paysage"
                        if joueur.paysages_riz <3 :
                            joueur.ajouter_points(joueur.paysages_riz+1)
                            joueur.paysages_riz += 1
                            message_box.text = "Vous avez reçu une carte paysage de rizière ! "
                        else :
                            message_box.text = "vous avez déjà le maximum de paysages rizière !"
                        message_box.text2=""
                        message_box.text3=""
                        message_box.text4=""
                        self.state = "avancer"

                    if case_joueur == "paysage_montagne":
                        self.state = "paysage"
                        if joueur.paysages_montagne <4 :
                            joueur.ajouter_points(joueur.paysages_montagne+1)
                            joueur.paysages_montagne += 1
                            message_box.text = "Vous avez reçu une carte paysage de montagne ! "
                        else :
                            message_box.text = "vous avez déjà le maximum de paysages montagne !"
                        message_box.text2=""
                        message_box.text3=""
                        message_box.text4=""

                    if case_joueur == "paysage_mer":
                        self.state = "paysage"
                        if joueur.paysages_mer < 5 :
                            joueur.ajouter_points(joueur.paysages_mer+1)
                            joueur.paysages_mer += 1
                            message_box.text = "Vous avez reçu une carte paysage de mer ! "
                        else :
                            message_box.text = "vous avez déjà le maximum de paysages mer !"
                        message_box.text2=""
                        message_box.text3=""
                        message_box.text4=""
            
                    if case_joueur == "source_chaude":
                        self.state = "source_chaude"
                        n= random.choice([2, 3])
                        joueur.ajouter_points(n)
                        joueur.sources_chaudes += 1 
                        message_box.text = "Vous avez gagné "+str(n)+" points en vous reposant dans une source chaude !"
                        message_box.text2=""
                        message_box.text3=""
                        message_box.text4=""
                        
                    if case_joueur == "ferme":
                        self.state = "ferme"
                        joueur.ajouter_pieces(3)
                        message_box.text = "Vous avez gagné 3 pièces en allant dans une ferme !"
                        message_box.text2=""
                        message_box.text3=""
                        message_box.text4=""
                        
                    
                    

                
                
                screen.fill((255,255,255))
                
                text1 = font2.render("Scores =", True, black)
                text2 = font2.render("Input Box:", True, black)
                text3 = font2.render("Message Box:", True, black)
                text_scores = ""
                for joueur in liste_joueurs :
                    text_scores += str(joueur)+" / "
                text_scoress = font2.render(text_scores, True, black)
                screen.blit(text_scoress, (100, 10))
                screen.blit(text1, (10, 10))
                screen.blit(text2, (10, 490))
                screen.blit(text3, (250, 490))
                
                
                def joueurr ():
                    self.cases_des_joueurs = []
                    for joueur in liste_joueurs:
                        self.cases_des_joueurs.append (joueur.case)
                        qui_va_jouer = min(self.cases_des_joueurs)
                    
                    for joueur in liste_joueurs :
                        if joueur.case == qui_va_jouer :
                            joueur_qui_va_jouer = joueur
                            return joueur_qui_va_jouer
                
                partie_finie()
                if self.state == "avancer":
                    message_box.text4 = "C'est à "+joueurr().nom+" de jouer, de combien de cases voulez-vous avancer"
                    message_box.text = ""
                    message_box.text2 = ""
                    message_box.text3 = ""
    
                Piste_1 = pygame.image.load("plateau1.png").convert_alpha()  
                
                screen.blit(Piste_1, Piste_1.get_rect(center = (self.longueur/2, self.largeur/2-50) ))
                input_box_jeu.draw(screen)
    
                message_box.draw(screen)
                bouton_valider3.draw(screen)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT :
                        self.running = False      
                    if event.type == pygame.MOUSEBUTTONDOWN :
                        if bouton_valider3.rect.collidepoint(event.pos): 
                           
                            if self.state == "echoppe":
                                achats = input_box_jeu.text
                                Echoppe2(joueur,utile, achats)
                              
                                for i in range(2):
                                    print(i+1)
                                    time.sleep(1)
                                    self.state = "avancer"
                                   

                            elif self.state == "temple":
                                dons = int(input_box_jeu.text)
                                self.temple.don2(joueur,dons)
        
                            elif self.state == "relais":
                                achete = int(input_box_jeu.text)
                                Relais2 (joueur,repas_achetables1,repas_achetables2,repas_achetables3,repas_achetables4,achete,utile)                               
                                message_box.text=""
                                message_box.text2=""
                                message_box.text3=""              

                            elif self.state == "avancer" :
                                avancement = int(input_box_jeu.text) 
                                utile = Jouer(joueurr(),avancement)                           
                            input_box_jeu.text = ""
                        
                    
                    input_box_jeu.handle_event(event)
                    if event.type == pygame.KEYDOWN:
                        input_box_jeu.draw(screen)
                        message_box.draw(screen)
                                        
                    pygame.display.flip()  
                
                
                pygame.display.flip()      

pygame.init()
pygame.display.set_caption('Tokaido')


screen = pygame.display.set_mode((x,y))
fond = pygame.image.load("thicc_tokaido_couverture.png").convert()
fond = pygame.transform.scale(fond, (600,600))
pygame.display.set_icon(fond)
game = Game(screen,x,y)

Bouton_play = pygame.image.load("Bouton_play.png").convert_alpha()
Bouton_play = pygame.transform.scale(Bouton_play, (150,80))

Bouton_exit = pygame.image.load("Bouton_exit.png").convert_alpha()
Bouton_exit = pygame.transform.scale(Bouton_exit, (150,80))
bouton_valider = Bouton(545,350,80,30,"Valider",screen)
bouton_valider2 = Bouton(670,20,80,30,"Valider",screen)
bouton_valider3 = Bouton(120,535,80,30,"Valider",screen)
bouton_regles = Bouton(x-130,50,80,30,"Règles",screen)
bouton_scores = Bouton(x-130,100,80,30,"Scores",screen)
bouton_retour = Bouton(30,50,80,30,"Retour",screen)
bouton_connexion = Bouton(500,15,110,30,"Connexion",screen)
bouton_inscription = Bouton(620,15,110,30,"Inscription",screen)

fond_co = pygame.image.load("fond_co.png").convert()

game.run(use_screen)
    
pygame.quit()