from manim import *
import numpy as np



class Bubble(Scene):
    
    def construct(self):
        title = TexMobject("Bubble Sort").scale(2)
        description = TextMobject(
            "Vertauscht benachbarte Elemente einer Liste \\\\ bis das maximale Element das Ende der Liste erreicht"
            ,organize_left_to_right=True
        )

        image_main = ImageMobject("main/Jade_Hochschule_logo.svg")
        self.play(FadeIn(image_main))
        self.wait(2)
        self.play(FadeOut(image_main))
        self.wait()



        VGroup(title,description).arrange(DOWN)        
        self.play(Write(title))
        self.play(Write(description))

        self.wait(5)    

        self.play(FadeOut(description))
        self.play(title.to_edge,UP )

        title_line = Line(title.get_right(), title.get_left()).scale(2).next_to(title, DOWN)
        self.play(Write(title_line))

        

        arr = [90, 80, 70, 60, 50, 40, 30, 20, 10]
        array = Array(arr)
        
        self.play(ShowCreation(array))
        self.wait()

        self.swap_values(array,arr)

        partitionline = Line(title_line.get_center(), DOWN*3)
        self.play(GrowFromCenter(partitionline))
        self.wait(2)


        self.write_algo()
        algo_step_2, algo_step_3, algo_swap, algo_end_inner_loop = self.write_algo()
        self.show_time_complexity(algo_step_2, algo_step_3, algo_swap, algo_end_inner_loop)
        

        
        self.wait()   
        self.clear()
        self.wait()

        self.aufgabe()
        



    


    def swap_values(self,array,arr):

        ind1 =0
        ind2 =1

        sort1 = array.create_index(ind1, color=YELLOW, show_label=False)
        sort2 = array.create_index(ind2, color=YELLOW, show_label=False)

        self.play(ShowCreation(sort1),ShowCreation(sort2))
        self.wait()

        n = len(arr)



        
        while sort1.get_value() < len(array.values) and sort2.get_value() < len(array.values):
                
                if array.values[sort1.get_value()] >= array.values[
                    sort2.get_value()]: 
                        
                    self.play(*sort1.animate_set_index(sort1.get_value() + 1),
                           *sort2.animate_set_index(sort2.get_value() + 1), runtime=1)
                    self.wait(2)
                        
                        
                else:                        
                        self.play(*sort1.animate_set_index(sort1.get_value()+ 1),
                            *sort2.animate_set_index(sort2.get_value()+ 1) , runtime=1)
                        self.wait(2)
    

        self.play(Uncreate(sort1), Uncreate(sort2))
        self.wait()
        self.play(FadeOut(array))
        



    def aufgabe(self):
        aufgabe = TextMobject("Aufgabe").scale(2)
        
        aufgabenstellung = TextMobject(
            "Stellen sie anhand von Pseudocode \\\\ den Bubblesort in C-sharp da!"
            ,organize_left_to_right=True
        )
        VGroup(aufgabe,aufgabenstellung).arrange(DOWN)        
        self.play(Write(aufgabe))
        self.play(Write(aufgabenstellung))
        self.wait(10)
        self.play(FadeOut(aufgabenstellung),FadeOut(aufgabe))
        self.wait()
    

    def write_algo(self):
        step1 =  TexMobject("Loop \\ for \\ i=0 \\ to \\ i=N-1").scale(0.8).to_edge(LEFT)
        step1.shift(UP*1.5)
        step2 =  TexMobject("Loop \\ for \\ j=0 \\ to \\ j=N-i-1").scale(0.8)
        step2.next_to(step1, DOWN).shift(RIGHT*0.5)
        step3 = TexMobject("if \\ arr[j] \\ > \\ arr[j+1]:").scale(0.8)
        step3.next_to(step2, DOWN).shift(RIGHT*0.5)
        swap = TexMobject("swap \\ arr[j] \\ and \\ arr[j+1]").scale(0.8).to_edge(LEFT)
        swap.next_to(step3, DOWN).shift(RIGHT*0.5)
        end_inner_loop = TexMobject("End \\ of \\ Inner \\ Loop").scale(0.8).next_to(swap, DOWN).shift(LEFT*1.9)
        end_outer_loop = TexMobject("End \\ of \\ Outer \\ Loop").scale(0.8).next_to(end_inner_loop, DOWN).to_edge(LEFT)

        self.wait(1.5)
        self.play(Write(step3))
        self.wait(1)
        self.play(Write(swap))
        self.wait(5.5)
        self.play(Write(step1),Write(end_outer_loop))
        self.wait(6.5)
        self.play(Write(step2),Write(end_inner_loop))
        self.wait(13)
        return ((step2,step3,swap,end_inner_loop))


    def show_time_complexity(self,algo_step_2, algo_step_3, algo_swap, algo_end_inner_loop):
        title = TextMobject(' Zeitkomplexitätsanalyse').scale(0.8).to_edge(RIGHT).shift(UP*2  + LEFT * 0.7)
        title_line = Line(title.get_right(), title.get_left()).next_to(title, DOWN)
        step_1 = TexMobject("(n-1)","+","(n-2)","+","(n-3)","+","...","+","1").scale(0.7).next_to(title_line, DOWN)
        step_2 = TexMobject("= \\frac{n(n-1)}{2} ").scale(0.8).next_to(step_1, DOWN).next_to(step_1, DOWN)
        step_3 = TexMobject("= \\frac{(n^2 - n)}{2}").scale(0.8).next_to(step_2, DOWN).next_to(step_2, DOWN)
        step_4 = TexMobject("= \\ O(n^2)").scale(0.8).next_to(step_3, DOWN).next_to(step_3, DOWN)
        inner_loop_group = VGroup(algo_step_2, algo_step_3, algo_swap, algo_end_inner_loop)

        self.play(Write(title), Write(title_line))
        self.wait()
        self.play(ShowPassingFlashAround(inner_loop_group))
        self.wait()
        for i in range(0,9,2):
            self.play(Transform(inner_loop_group.copy(),step_1[i:i+2]))
            self.wait(2)
        self.wait(4)
        self.play(ReplacementTransform(step_1.copy(), step_2))
        self.wait(6)
        self.play(ReplacementTransform(step_2.copy(),step_3)) 
        self.wait(6)
        self.play(ReplacementTransform(step_3.copy(), step_4))
        self.wait(3)





class ArrayIndex(VGroup):
    """
    Visualization of an array index.
    Includes a highlighting rectangle for the array element, and option pointer and label
    with index value.
    """

    CONFIG = {
        'wdith': 1,
        'height': 1,
        'name': 'i',
        'color': BLUE,
        'opacity': 0.75,
        'position': DOWN,
        'show_arrow': True,
        'show_label': True,
    }

    def __init__(self, parent, value, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)
        self.parent = parent
        self.index_tracker = ValueTracker(value)
        self.indicator_box = self.add_indicator_box()
        if self.show_label:
            self.label = always_redraw(lambda: self.get_label())
        else:
            self.label = None
            self.show_arrow = False  # No arrow without label
        if self.show_arrow:
            self.arrow = always_redraw(lambda: self.get_arrow())
        else:
            self.arrow = None
        self.add(*remove_nones([self.label, self.arrow, self.indicator_box]))

    def add_indicator_box(self):
        box = Rectangle(width=self.width - 0.1, height=self.height - 0.1)
        box.set_stroke(color=self.color,
                       opacity=self.get_box_opacity(self.get_value()))
        box.move_to(self.get_box_target(self.get_value()))
        return box

    def get_label(self):
        i = int(round(self.index_tracker.get_value(), 0))
        ni = TextMobject(self.name + '=' + str(i))
        ni.next_to(self.indicator_box, self.position, LARGE_BUFF)
        return ni

    def get_arrow(self):
        if self.label.get_y() < self.indicator_box.get_y():
            a = Arrow(self.label.get_top(),
                      self.indicator_box.get_bottom(),
                      buff=MED_SMALL_BUFF)
        else:
            a = Arrow(self.label.get_bottom(),
                      self.indicator_box.get_top(),
                      buff=MED_SMALL_BUFF)
        return a

    def set_index(self, value):
        self.indicator_box.set_stroke(opacity=self.get_box_opacity(value))
        self.indicator_box.move_to(self.get_box_target(value))
        self.index_tracker.set_value(value)
        return self

    def get_box_target(self, value):
        if value < 0:
            fpe_o = self.parent.elements[0].get_critical_point(ORIGIN)
            return fpe_o + LEFT * self.width
        elif value < len(self.parent.elements):
            return self.parent.elements[value].get_critical_point(ORIGIN)
        else:
            lpe_o = self.parent.elements[-1].get_critical_point(ORIGIN)
            return lpe_o + RIGHT * self.width

    def get_box_opacity(self, value):
        if 0 <= value < len(self.parent.elements):
            return self.opacity
        else:
            return 0.5

    def animate_set_index(self, value):
        return [
            self.indicator_box.set_stroke,
            {
                'opacity': self.get_box_opacity(value),
                'family': False
            },
            self.indicator_box.move_to,
            self.get_box_target(value),
            self.index_tracker.set_value,
            value,
        ]

    def get_value(self):
        return int(self.index_tracker.get_value())


class Array(VGroup):
    """
    Visualization of an array wwith elements, an outline, and optional multiple indices.
    """

    CONFIG = {
        'element_width': 0.6,
        'element_height': 0.6,
        'element_color': WHITE,
        'show_labels': True,
        'labels_scale': 0.5,
    }

    def __init__(self, values, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        self.values = values
        self.indicies = {}

        self.total_width = self.element_width * len(self.values)
        self.hw = self.element_width / 2
        self.hh = self.element_height / 2
        self.left_element_offset = (self.total_width / 2) - self.hw
        self.left_edge_offset = self.left_element_offset + self.hw

        # Add the outline of the array.
        self.outline = VGroup()
        self.outline.add(self.create_bounding_box())

        # Add separators between the elements
        separators = VGroup()
        for i in range(1, len(self.values)):
            x = i * self.element_width
            separators.add(
                Line([x, -self.hh, 0], [x, self.hh, 0], stroke_width=2))
        separators.shift(LEFT * self.left_edge_offset)
        self.outline.add(separators)
        self.add(self.outline)

        # Add each element as a string, in order, spaced accordingly.
        self.elements = VGroup()
        self.backgrounds = VGroup()
        for i, v in enumerate(values):
            if v is not None:
                t = TextMobject(str(v))
            else:
                t = TexMobject('.', width=0, height=0, color=BLACK)
            t.move_to(i * RIGHT * self.element_width)
            self.elements.add(t)
            b = Rectangle(width=self.element_width - 0.1,
                          height=self.element_height - 0.1)
            b.set_stroke(color=BLACK, opacity=0)
            b.move_to(t.get_center())
            self.backgrounds.add(b)
        self.backgrounds.shift(LEFT * self.left_element_offset)
        self.add(self.backgrounds)
        self.elements.shift(LEFT * self.left_element_offset)
        self.elements.set_color(self.element_color)
        self.add(self.elements)

        # Add labels for the array, centered under each element.
        if self.show_labels:
            self.labels = VGroup()
            for i in range(len(self.values)):
                label = TextMobject(str(i)).scale(self.labels_scale)
                label.move_to((i * RIGHT * self.element_width) +
                              (UP * self.element_height * 0.8))
                self.labels.add(label)
            self.labels.shift(LEFT * self.left_element_offset)
            self.add(self.labels)

    def create_bounding_box(self):
        return Rectangle(width=self.total_width,
                         height=self.element_height,
                         stroke_width=2)

    def create_index(self, value, **kwargs):
        i = ArrayIndex(self,
                       value,
                       width=self.element_width,
                       height=self.element_height,
                       **kwargs)
        self.add(i)
        return i

    def remove_index(self, index):
        self.remove(index)

    def hide_labels(self):
        self.show_labels = False
        self.remove(self.labels)

