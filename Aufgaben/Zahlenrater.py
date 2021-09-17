from manimlib.imports import *


class zahlenraten(Scene):
    def construct(self):

        image_main = ImageMobject("main/Jade_Hochschule_logo.svg")

        title = TextMobject("Zahlenraten").scale(2)
        description = TextMobject(
            "Ein programm bei dem der Benutzer eine festgelegte Zahl \\\\ erraten muss bei jeder Eingabe, soll der Benutzer ein feedback bekommen \\\\ (Höher, Tiefer)"
            ,organize_left_to_right=True).scale(0.8)
        VGroup(title,description).arrange(DOWN)  

        self.play(FadeIn(image_main))
        self.wait(2)
        self.play(FadeOut(image_main))
        self.wait()

        self.play(Write(title))     
        self.play(Write(description)) 
        self.wait(5)    
        self.play(FadeOut(description))
        self.play(title.to_edge,UP ) 
        self.wait()

        title_line = Line(title.get_right(), title.get_left()).scale(2).next_to(title, DOWN)
        self.play(Write(title_line))

        partitionline = Line(title_line.get_center(), DOWN*3)
        self.play(GrowFromCenter(partitionline))
        self.wait(2)

        self.showcode(title_line)


        self.wait()   
        self.clear()
        self.wait()

        self.aufgabe()
        
        

    def showcode(self, title_line):
        int1 =  TexMobject("geheimzahl \\ = \\ 69").scale(0.5).next_to(title_line, DOWN).to_edge(LEFT)
        int2 =  TexMobject("versuch \\ = \\ -1").scale(0.5).to_edge(LEFT).next_to(int1,DOWN).shift(LEFT*0.2)
        int3 =  TexMobject("zaehler \\ = \\ 0").scale(0.5).to_edge(LEFT).next_to(int2,DOWN).shift(LEFT*0.1)

        while1 =  TexMobject("while \\ versuch \\ != \\ geheimzahl: ").scale(0.5).next_to(int3,DOWN*2.5).to_edge(LEFT)
        step1 =  TexMobject("versuch \\ = \\ int(input('Bitte Raten'))").scale(0.5).next_to(while1,DOWN).to_edge(LEFT).shift(RIGHT*0.5)

        step2 = TexMobject("if \\ versuch \\ < \\ geheimzahl:").scale(0.5).next_to(step1,DOWN).to_edge(LEFT).shift(RIGHT*0.5)
        step3 =  TexMobject("print('Hoeher') ").scale(0.5).next_to(step2,DOWN).to_edge(LEFT).shift(RIGHT*0.5)

        step4 = TexMobject("if \\ versuch \\ > \\ geheimzahl:").scale(0.5).next_to(step3,DOWN).to_edge(LEFT).shift(RIGHT*0.5)
        step5 =  TexMobject("print('Tiefer') ").scale(0.5).next_to(step4,DOWN).to_edge(LEFT).shift(RIGHT*0.5)

        step6 = TexMobject("zaehler \\ = \\ zaehler \\ + \\ 1 ").scale(0.5).next_to(step5,DOWN).to_edge(LEFT).shift(RIGHT*0.5)

        end = TexMobject("print('sie \\ haben ' \\ zaehler \\ ' versuche \\ gebraucht')").scale(0.5).next_to(step6,DOWN).to_edge(LEFT)


        while2 = TextMobject(
            "Die Anweisung while führt \\\\ eine Anweisung oder einen Anweisungsblock aus, \\\\ während ein angegebener boolescher \\\\ Ausdruck true ergibt.").scale(0.5).next_to(title_line, DOWN*2).to_edge(RIGHT)
        
        if1 = TextMobject(
            "Eine if -Anweisung ermittelt, \\\\ welche Anweisung basierend auf dem Wert \\\\ eines booleschen Ausdrucks auszuführen ist.").scale(0.5).next_to(while2, DOWN*2).to_edge(RIGHT)

        

        self.play(Write(int1), Write(int2), Write(int3))
        self.wait(5)
        self.play(Write(while1), Write(step1))
        self.play(Write(while2))
        self.wait(15)
        self.play(Write(step2), Write(step3))
        self.play(Write(if1))
        self.wait(15)
        self.play(Write(step4), Write(step5))
        self.wait(5)
        self.play( Write(step6))
        self.wait(5)
        self.play( Write(end))
        self.wait(5)
        





    

    def aufgabe(self):
        aufgabe = TextMobject("Aufgabe").scale(2)
        
        aufgabenstellung = TextMobject(
            "Schreiben sie einen Zahlenrater in C-sharp Syntax!"
            ,organize_left_to_right=True
        )
        VGroup(aufgabe,aufgabenstellung).arrange(DOWN)        
        self.play(Write(aufgabe))
        self.play(Write(aufgabenstellung))
        self.wait(10)
        self.play(FadeOut(aufgabenstellung),FadeOut(aufgabe))
        self.wait()