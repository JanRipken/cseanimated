from manimlib.imports import *


class whatsinfo(Scene):
    def construct(self):

        title = TextMobject("Was ist Informatik").scale(1.5)

        definition_1 = TextMobject("Definition 1:").to_edge(UP)
        definition_2 = TextMobject("Definition 2:").to_edge(UP)
        definition1 = TextMobject("Informatik ist die Wissenschaft von der systematischen Verarbeitung von Informationen, besonders der automatischen, mit Hilfe von Computern.",organize_left_to_right=True).scale(0.8)
        definition2 = TextMobject("Informatik ist die Wissenschaft, Technik und Anwendung der maschinellen Verarbeitung und Übermittlung von Informationen",organize_left_to_right=True).scale(0.8)



        self.play(FadeIn(title))
        self.wait()
        self.play(FadeOut(title))
        self.wait()

        self.play(FadeIn(definition_1))
        self.wait()
        self.play(FadeIn(definition1))
        self.wait(10)
        self.play(Transform(definition_1,definition_2), Transform(definition1,definition2))
        self.wait(10)
        self.play(FadeOut(definition_1), FadeOut(definition1))
        self.wait()

        techinf = TextMobject("Technische Informatik:",color=ORANGE)
        techinf_info = TextMobject("Befasst sich mit der inneren Struktur, dem Bau von Computern und allen damit zusammenhängenden technischen Fragen")
        techinf_grp = VGroup(techinf, techinf_info).arrange(DOWN).to_edge(UP).scale(0.7)
        techinf_brd = SurroundingRectangle(techinf_grp,color=WHITE)
        techinf_grp2 = VGroup(techinf_grp, techinf_brd)

        self.play(FadeIn(techinf_grp2))
        self.wait(10)

        prakinf = TextMobject("Praktische Informatik:",color=ORANGE)
        prakinf_info = TextMobject("Umfasst die Prinzipien und Techniken der Programmierung")
        prakinf_grp = VGroup(prakinf, prakinf_info).arrange(DOWN).to_edge(UP).scale(0.7).next_to(techinf_grp2, DOWN)
        prakinf_brd = SurroundingRectangle(prakinf_grp,color=WHITE)
        prakinf_grp2 = VGroup(prakinf_grp, prakinf_brd)

        self.play(FadeIn(prakinf_grp2))
        self.wait(10)


        angeinf = TextMobject("Angewandte Informatik:",color=ORANGE)
        angeinf_info = TextMobject("Bildet die Brücke zwischen Methoden der Informatik und Anwendungsproblemen")
        angeinf_grp = VGroup(angeinf, angeinf_info).arrange(DOWN).to_edge(UP).scale(0.7).next_to(prakinf_grp2, DOWN)
        angeinf_brd = SurroundingRectangle(angeinf_grp,color=WHITE)
        angeinf_grp2 = VGroup(angeinf_grp, angeinf_brd)

        self.play(FadeIn(angeinf_grp2))
        self.wait(10)


        theoinf = TextMobject("Theoretische Informatik:",color=ORANGE)
        theoinf_info = TextMobject("Entwickelt Mathematische Modelle von Computern und Hilfsmittel zu ihrer präziesen Beschreibung")
        theoinf_grp = VGroup(theoinf, theoinf_info).arrange(DOWN).to_edge(UP).scale(0.7).next_to(angeinf_grp2, DOWN)
        theoinf_brd = SurroundingRectangle(theoinf_grp,color=WHITE)
        theoinf_grp2 = VGroup(theoinf_grp, theoinf_brd)

        self.play(FadeIn(theoinf_grp2))
        self.wait(10)

        self.play(FadeOut(techinf_grp2),FadeOut(prakinf_grp2),FadeOut(angeinf_grp2),FadeOut(theoinf_grp2))
        self.wait()
        