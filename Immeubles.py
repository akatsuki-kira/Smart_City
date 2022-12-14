from random import *
from turtle import *


class Immeuble:

    def __init__(self, Etages: tuple, Position: tuple) -> None:
        """
        On crée un objet avec Immeuble qui prend en paramètre le nombre d'étage et la sa position sur le plan.
        """
        self.etages = Etages
        self.position = Position
        

    #On crée des méthodes pour récuperer les attributs de la class.
    def get_etage(self):
        """
        La méthode renvoie le nombre d'étage passé en paramettre depuis la création de l'objet Immeuble.
        """
        return self.etages

    def get_position(self):
        """
        La méthode renvoie la position.
        Point de départ de la construction de la ville.
        """
        return self.position

    def move(self, position: tuple):
        """
        La fonction move déplace le curseur vers une nouvelle position
        En prenant garde de ne pas laisser de trace pendant le déplacement.
        """
        penup()
        setposition(position[0], position[1])
        pendown()

    def triangle(self, color: str):
        """
        Prend en paramettre une couleur et dessine un toit sous dorme d'un triangle non-equilatéral.
        """
        begin_fill()
        fillcolor(color)
        forward(110)
        left(140)
        forward(72)
        left(80)
        forward(72)
        left(140)
        end_fill()

    def fenetre(self):
        """
        Dessine un rectangle debout de 30px de haut et de 20px de large de couleur blanc.
        Correspond à une fenêtre sur le dessin.
        """
        begin_fill()
        fillcolor('white')
        for i in range(2):
            forward(20)
            left(90)
            forward(30)
            left(90)
        end_fill()

    def balcon(self, position):
        """
        Prend en paramètre la position d'une fenêtre et dessine un grillage autour de la fenêtre.
        Correspond à un balcon sur le dessin.
        """
        width(3)
        penup()
        setposition(position[0]-4, position[1])
        pendown()
        forward(28)
        penup()
        setposition(position[0]-4, position[1]+10)
        pendown()
        for i in range(4):
            right(90)
            forward(10)
            backward(10)
            left(90)
            forward(7)
        right(90)
        forward(10)
        backward(10)
        left(90)
        penup()
        setposition(position[0], position[1])
        pendown()
        width(1)


    def porte_en_arc(self, x, color):
        """
        La fonction prend en paramettre la largeur de la porte et sa couleur.
        Elle dessine une porte de la taille et couleur correspondante.
        """
        fillcolor(color)
        begin_fill()


        right(180)
        penup()
        fd(x/2)
        pendown()
        left(90)
        fd(x)
        left(90)
        fd(x/2)
        left(90)
        fd(x)
        left(90)
        penup()
        fd(x/2)
        pendown()
        right(180)
        
        #Arc de cercle:
        penup()
        right(90)
        fd(x/4)
        left(90)
        fd(x/4)
        circle(x/4,extent = 90)
        pendown()
        circle(x/4,extent = 180)


        end_fill()

        left(90)


    def solar_panel(self, longueur,x,y):
        """
        Dessine un panneau solaire en fonction de la longueur et de la position.
        """
        penup()
        setpos(x,y)
        pendown()
        color("#818589")
        begin_fill()
        fillcolor("#818589")
        pos1 = pos()
        fd(longueur*3)
        left(90)
        fd(longueur/2)
        left(90)
        fd(5/4*longueur) #-------
        right(90)
        fd(longueur*5/2)  # coté  barre
        left(90) #TOIT DU PANNEAU
        fd(longueur/2)  # TOIT DU PANNEAU
        left(90) # TOIT DU PANNEAU
        fd(longueur/2)  #coté barre
        z =pos()
        fd(8/4*longueur) # côté barre
        right(90)
        fd(5/4*longueur)#------
        left(90)
        fd(longueur/2)
        penup()
        setpos(z)
        pendown()
        left(135)
        end_fill()
        begin_fill()
        color("#0047AB")
        fillcolor("#0047AB")
        fd(longueur*2)
        left(90)
        fd(longueur/2)
        left(90)
        fd(longueur*4)
        left(90)
        fd(longueur/2)
        left(90)
        fd(longueur*2)
        right(45)
        self.move(pos1)
        end_fill()
        color('black')

    def flag(self, pos: tuple):
        """
        Prend une position en paramètre et dessine un drapeau à la position passé en paramètre 
        Dessine un drapeau LGBT
        """
        self.move(pos)
        left(90)
        width(5)
        fd(40)
        width(1)
        right(90)
        for i in range(6):
            color(["#FF0018", "#FFA52C", "#FFFF41", "#008018", "#0000F9", "#86007D"][i])
            self.rectangle(40, 3, ["#FF0018", "#FFA52C", "#FFFF41", "#008018", "#0000F9", "#86007D"][i])
            penup()
            left(90)
            backward(3)
            right(90)
            pendown()
        color('black')



    def porte(self, color: str):
        """
        Prend en paramètre un str, couleur.
        Dessine un rectangle debout de 30px de haut et de 20px de large de la couleur passée en paramètre.
        Correspond à une porte sur le dessin.
        """
        begin_fill()
        fillcolor(color)
        for i in range(2):
            forward(20)
            left(90)
            forward(30)
            left(90)
        end_fill()


    def rectangle(self, x: int, y: int, color: str):
        """
        Prend en paramètre la largeur et la longueur et la couleur de remplissage de la forme.
        Dessine un rectangle en fonction des paramettres corespondant.
        """
        begin_fill()
        fillcolor(color)
        for i in range(2):
            forward(x)
            left(90)
            forward(y)
            left(90)
        end_fill()


    def draw(self):
        """
        La fonction draw permet de dessiner un immeuble sur le plan, 
        Elle génére aléatoirement la couleur à partir d'un palette prédéfinie.
        """
        #On définie la position et les attribus du curseur
        self.move(self.get_position())

        color = choice(['#430C05', '#D46F4D', '#FFBF66', '#08C5D1', '#00353F'])

        self.rectangle(100, 50*self.get_etage(), color)
        for i in range(self.get_etage()):
            color = choice(['#430C05', '#D46F4D', '#FFBF66', '#08C5D1', '#00353F'])
            

            #On dessine les fenêtres
            if i > 0:                     #A l'étage 0 on dessine pas de fenêtre, mais une porte.
                self.move((pos()[0], pos()[1]+ 10)) #Met la fenêtre au milieu de l'étage.
                for j in range(3):
                    self.move((pos()[0] + 25 , pos()[1]))
                    if choice([True, True, False, True]): #2 chance sur 3 de dessiner une fenêtre
                        self.fenetre()
                        if choice([True, False]):   #1 chance sur 2 de générer un balcon à la fenêtre
                            self.balcon(pos())

            #Ici on dessine la porte.
            else:
                color = choice(['#FFF4BD', '#F4B9B8', '#85D2D0', '#887BB0'])    #On change la palette de couleur pour les portes
                
                if choice([False, True]):   #Une chance sur deux de dessiner une porte carré
                    self.move((pos()[0] + 15* randint(1,4) , pos()[1])) #On donne un décalage aléatoire aux portes
                    self.porte(color)
                else:                       #Une chance sur deux de dessiner une porte arrondie
                    self.move((pos()[0] + 25 * randint(1,3) , pos()[1]+30)) 
                    self.porte_en_arc(30, color)
            self.move((self.get_position()[0] - 5, self.get_position()[1] + 50 + 50*i))
        
        #On laisse une chance sur deux de généré un toit en triangle, sinon une térasse
        color = choice(['#430C05', '#D46F4D', '#FFBF66', '#08C5D1', '#00353F'])
        if choice([False, True]):
            self.rectangle(110, 10, color)
            top_pos = pos()                 #On sauvegarde la position en haut du toit avant de dessiner les panneaux solaires.
            for i in range(3):  #3 fois sur le toit on va donner une chance sur deux de dessiner un panneau solaire.
                if i == 2 and choice([True, True, False]):
                    self.flag((top_pos[0] + 15 + 30*i, top_pos[1]+ 10))
                elif choice([True, False]):   
                    self.solar_panel(10, top_pos[0] + 10 + 30*i, top_pos[1]+ 10)    #On décale le curseur de 10px vers le haut et de 10px vers la droite.
                
        else:
            self.triangle(color)



class Ville:
    def __init__(self, nb_batiments, immeuble) -> None:
        """
        On définie un objet ville qui prend en paramettre le nombre de batiment et le type d'immeuble à dessiner.
        """
        self.nb_batiments = nb_batiments
        self.immeuble = immeuble

    def init(self, position: tuple):
        """
        Prend en paramètre la vitesse et la position de départ.
        Etablie la vitesse et positionne le curseur en position.
        """
        bgcolor('#87CEEB')
        pencolor('black')        #On définie la couleur
        speed(100)                
        width(1)                 #L'épaisseur du crayon
        penup()                  #On initialise le crayon comme levé pour les premiers déplacements.
        setpos(position[0], position[1])


    def boulangerie(self, position: tuple):
        """
        Dessine une boulangerie a la position passé en paramettre.
        """
        self.immeuble.move((position[0], position[1]))
        self.immeuble.rectangle(100, 50, '#9C254D')

        self.immeuble.move((position[0]+10, position[1]+10))
        self.immeuble.fenetre()

        self.immeuble.move((position[0]+50, position[1]))
        self.immeuble.porte('#D6E4E5')
        self.immeuble.move((position[0], position[1]+50))

        self.immeuble.rectangle(100, 20, '#FFF6BF')
        forward(2)
        write( choice(["Boulangerie", "Coiffeur", "Libraire", "Boucherie"]), font=("JetBrains Mono",11, "normal"))

    def floor(self, largeur):
        """
        Prend en paramètre la largeur de la ville (entier) et dessine un bloc vert qui va supporter la ville.
        La longueur du bloc s'adapte au nombre d'immeubles de la ville.
        """
        #On dessine l'herbe
        begin_fill()
        color('#116530',  '#116530')    #Nuance de vert
        penup()
        setpos(self.immeuble.get_position()[0]-10, self.immeuble.get_position()[1]- 80)
        pendown()
        self.immeuble.rectangle(10 + 120*largeur, 100, '#116530')   #La taille du rectangle s'adapte à la longueur de la ville (nb de batiments)
        penup()
        setpos((self.immeuble.get_position()[0]-10, self.immeuble.get_position()[1]- 60))
        pendown()
        self.immeuble.rectangle(10 + 120*largeur, 31, '#333533')
        end_fill()

        #Route
        setpos((self.immeuble.get_position()[0]-10, self.immeuble.get_position()[1]- 45))
        width(3)
        color('white')
        for i in range(largeur):
            penup()
            forward(60)
            pendown()
            forward(60)

        #Voitures
        decalage = randint(1, 10*largeur)* 10
        self.immeuble.move((self.immeuble.get_position()[0]+5 + decalage, self.immeuble.get_position()[1]- 15))
        width(1)
        color('black')
        begin_fill()
        right(90)
        self.immeuble.rectangle(20,40, '#21B6A8')
        self.immeuble.move((self.immeuble.get_position()[0]+7 + decalage, self.immeuble.get_position()[1]- 17)) #Vitres
        self.immeuble.rectangle(10,15, '#6af3cf')
        self.immeuble.move((self.immeuble.get_position()[0]+28 + decalage, self.immeuble.get_position()[1]- 17))
        self.immeuble.rectangle(10,15, '#6af3cf')
        self.immeuble.move((self.immeuble.get_position()[0]-10 + decalage, self.immeuble.get_position()[1]- 25))
        self.immeuble.rectangle(20,80, '#21B6A8')
        self.immeuble.move((self.immeuble.get_position()[0]+58 + decalage, self.immeuble.get_position()[1]- 27)) #Feux avants
        self.immeuble.rectangle(10,10, '#f2e743')

        end_fill()
        self.immeuble.move((self.immeuble.get_position()[0]-5 + decalage, self.immeuble.get_position()[1]- 50))
        begin_fill()
        color('black')
        circle(10)
        self.immeuble.move((self.immeuble.get_position()[0]+45 + decalage, self.immeuble.get_position()[1]- 50))
        circle(10)
        end_fill()
        left(90)

        #Soleil
        self.immeuble.move((-350, 250))
        color('Yellow', 'Yellow')
        begin_fill()
        circle(75)
        end_fill()
        color('black')

    def lampadaires(self, decalage):
        """
        Dessine un lampadaire en fonction d'un décalage par rapport au debut du plan.
        """
        color('#403d39','#403d39')
        begin_fill()
        self.immeuble.move((self.immeuble.get_position()[0]-10 + decalage, self.immeuble.get_position()[1]+0))
        self.immeuble.rectangle(5,45, '#403d39')
        self.immeuble.move((self.immeuble.get_position()[0]-10 + decalage, self.immeuble.get_position()[1]+45))
        self.immeuble.rectangle(5,10, 'yellow')


    def arbre(self, decalage):
        """
        Dessine un arbre en fonction d'un décalage par rapport au debut du plan.
        """
        color('#673d13')
        begin_fill()
        self.immeuble.move((self.immeuble.get_position()[0]+10 + decalage, self.immeuble.get_position()[1]- 80))
        self.immeuble.rectangle(10,45, '#673d13')
        self.immeuble.move((self.immeuble.get_position()[0]+15 + decalage, self.immeuble.get_position()[1]- 35))
        end_fill()
        begin_fill()
        color('green')
        circle(30)
        end_fill()
        return decalage

    def lampadaires(self, decalage):
        """
        Dessine un lampadaire en se décalant par rapport à l'immeuble qu'il vient de dessiner.
        """

        color('#403d39','#403d39')

        begin_fill()

        self.immeuble.move((self.immeuble.get_position()[0]-10 + decalage, self.immeuble.get_position()[1]+0))

        self.immeuble.rectangle(5,45, '#403d39')

        self.immeuble.move((self.immeuble.get_position()[0]-10 + decalage, self.immeuble.get_position()[1]+45))

        self.immeuble.rectangle(5,10, 'yellow')


    def dessine(self):
        """
        La méthode dessine la ville en appellant les méthodes de la classe Immeuble pour dessiner 1 à 1 les Immeubles.
        """
        self.floor(self.nb_batiments) #On dessine le sol.    
        isboulangerie = 0   #Initialise le nb de boulangerie à 0
        self.init((self.immeuble.get_position()[0], self.immeuble.get_position()[1]))
        for i in range(self.nb_batiments):
            x = 120 * i

            if randint(1,3) == 3 and isboulangerie == 0:
                isboulangerie = 1
                self.boulangerie((self.immeuble.get_position()[0] + x, self.immeuble.get_position()[1]))
            else:
                Immeuble(
                    randint(self.immeuble.get_etage()[0],self.immeuble.get_etage()[1]),         #Nombre d'étages
                    (self.immeuble.get_position()[0] + x, self.immeuble.get_position()[1])      #Position de l'immeuble actuel
                        ).draw()                                                                #On démarre le dessin de l'immeuble    
        for i in range(self.nb_batiments+1):
            self.lampadaires(i*120)
            if i == self.nb_batiments:
                pass
            else:
                self.arbre(i*120)
        hideturtle()

