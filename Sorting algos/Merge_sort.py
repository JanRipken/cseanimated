from manimlib.imports import *


# Base class for all merge sort scenes, with support for a basic merge viz, and multi-level merge viz.
class MergeSortScenes(Scene):

    def __init__(self, **kwargs):
        self.merge_element_count = 0
        self.merge_current_level = 0
        self.merge_runtime = 1.0
        Scene.__init__(self, **kwargs)

    def construct(self):
        pass

    def merge_level_pair_begin(self, index):
        pass

    def merge_level_pair_end(self, index):
        pass

    def merge_level_extra_begin(self, index, extra):
        pass

    def merge_level_extra_end(self, index, extra):
        pass

    def merge_level(self, current_level, height, buff=SMALL_BUFF, speedy=False):
        new_level = VGroup()
        self.merge_current_level += 1
        for i in range(0, len(current_level), 2):
            if i + 1 < len(current_level):
                self.merge_level_pair_begin(i)
                left = current_level[i]
                right = current_level[i + 1]
                orig_group = VGroup(left, right)
                left = left.deepcopy()  # Leave the old ones in place, unharmed
                right = right.deepcopy()
                merged = Array([None] * (len(left.values) + len(right.values)),
                            show_labels=False)
                if height > 3:
                    merged.to_edge(TOP, buff=0.4)
                else:
                    merged.to_edge(TOP)
                halves = VGroup(left, right)
                if speedy:
                    self.play(
                        halves.arrange,
                        RIGHT,
                        {'buff': LARGE_BUFF},
                        halves.next_to,
                        merged,
                        DOWN,
                        ShowCreation(merged),
                        run_time=self.merge_runtime,
                    )
                else:
                    self.play(
                        halves.arrange,
                        RIGHT,
                        {'buff': LARGE_BUFF},
                        halves.next_to,
                        merged,
                        DOWN,
                        run_time=self.merge_runtime,
                    )
                    self.play(ShowCreation(merged))
                self.animate_merge(left, right, merged)
                self.play(merged.next_to,
                        orig_group,
                        UP, {'buff': buff},
                        run_time=self.merge_runtime)
                self.merge_level_pair_end(i)
            else:
                self.merge_level_extra_begin(i, current_level[i])
                merged = current_level[i].deepcopy()
                self.play(merged.next_to,
                        current_level[i],
                        UP, {'buff': buff},
                        run_time=self.merge_runtime)
                self.merge_level_extra_end(i, merged)
            new_level.add(merged)
        return new_level

    # dst[di] = src[si]
    def animate_merge_element(self, src, si, dest, di):
        self.merge_element_count += 1
        sec = src.elements[si.get_value()].copy()
        self.play(
            sec.move_to,
            dest.elements[di.get_value()],
            run_time=self.merge_runtime,
        )
        dest.elements.submobjects[di.get_value()] = sec
        dest.values[di.get_value()] = src.values[si.get_value()]
        self.play(
            *si.animate_set_index(si.get_value() + 1),
            *di.animate_set_index(di.get_value() + 1),
            run_time=self.merge_runtime,
        )

    def setup_animate_merge(self, left, right, merged):
        left_l = left.create_index(0, color=YELLOW, name='l')
        right_r = right.create_index(0, color=YELLOW, name='r')
        self.play(ShowCreation(left_l), ShowCreation(right_r))
        merged_m = merged.create_index(0, color=YELLOW, name='m', position=UP)
        self.play(ShowCreation(merged_m))
        self.wait()
        return left_l, right_r, merged_m

    def cleanup_animate_merge(self, left, left_l, right, right_r, merged,
                            merged_m):
        self.play(
            Uncreate(left_l),
            Uncreate(right_r),
            Uncreate(merged_m),
        )
        left.remove_index(left_l)
        right.remove(right_r)
        merged.remove_index(merged_m)
        self.play(FadeOutAndShift(left, UP + RIGHT),
                FadeOutAndShift(right, UP + LEFT))

    def animate_merge(self, left, right, merged):
        left_l, right_r, merged_m = self.setup_animate_merge(
            left, right, merged)

        while left_l.get_value() < len(
                left.values) and right_r.get_value() < len(right.values):
            if left.values[left_l.get_value()] <= right.values[
                    right_r.get_value()]:
                self.animate_merge_element(left, left_l, merged, merged_m)
            else:
                self.animate_merge_element(right, right_r, merged, merged_m)

        while left_l.get_value() < len(left.values):
            self.animate_merge_element(left, left_l, merged, merged_m)

        while right_r.get_value() < len(right.values):
            self.animate_merge_element(right, right_r, merged, merged_m)

        self.cleanup_animate_merge(left, left_l, right, right_r, merged,
                                merged_m)



class MergeFirstExample(MergeSortScenes):

    def construct(self):
        skip_to = 0

        t1 = TextMobject('Können wir zwei sortierte Arrays zu einem zusammenführen ?')
        t1.shift(UP)

        self.add(t1)
        self.wait()

        left = Array([2, 3, 4, 6], element_color=BLUE_D)
        right = Array([1, 3, 7, 8], element_color=LIGHT_BROWN)
        merged = Array([None] * 8)
        halves = VGroup(left, right).arrange(RIGHT, buff=LARGE_BUFF)


        self.play(t1.to_edge, UP, ShowCreation(left), ShowCreation(right))
        self.wait()

        if skip_to < 1:
            self.play(
                LaggedStartMap(CircleIndicate,
                            left.elements,
                            run_time=2,
                            lag_ration=0.7))
            self.play(
                LaggedStartMap(CircleIndicate,
                            right.elements,
                            run_time=2,
                            lag_ration=0.7))
            self.wait()


        merged.shift(UP * 1.5)
        self.play(
            halves.next_to,
            merged,
            DOWN,
            MED_LARGE_BUFF,
            FadeInFromDown(merged),
        )
        self.wait()

        self.play(left.shift, LEFT * 2.5, right.shift, RIGHT * 2.5)
        comp = TexMobject('links', '<=', 'rechts')
        comp.next_to(merged, BOTTOM, SMALL_BUFF)
        self.play(Write(comp))
        self.wait()

        comp_text = TextMobject('links[l]', ' <= ', 'rechts[r]')
        comp_text.next_to(merged, BOTTOM, SMALL_BUFF)

        self.play(ReplacementTransform(comp, comp_text))
        self.wait()

        left_l = left.create_index(0, color=YELLOW, name='l')
        right_r = right.create_index(0, color=YELLOW, name='r')
        self.play(ShowCreation(left_l), ShowCreation(right_r))
        self.wait()

        merged_m = merged.create_index(0, color=YELLOW, name='m', position=UP)
        self.play(
            ShowCreation(merged_m),
            t1.to_edge,
            UP,
            {'buff': SMALL_BUFF},
        )
        self.wait()

        llo = -1
        rro = -1
        while left_l.get_value() < len(
                left.values) and right_r.get_value() < len(right.values):
            self.merge_element_count += 1

            if self.merge_element_count == 3:
                self.play(FadeOut(sort_text))

            ll = left_l.get_value()
            rr = right_r.get_value()
            if ll != llo:
                llo = ll
                lc = left.elements[ll].copy()
            if rr != rro:
                rro = rr
                rc = right.elements[rr].copy()
            if comp_text[0] != lc:
                self.play(lc.move_to,
                        comp_text[0],
                        Uncreate(comp_text[0]),
                        run_time=self.merge_runtime)
                comp_text.submobjects[0] = lc
            if comp_text[2] != rc:
                self.play(rc.move_to,
                        comp_text[2],
                        Uncreate(comp_text[2]),
                        run_time=self.merge_runtime)
                comp_text.submobjects[2] = rc
            self.wait(duration=self.merge_runtime)


            if self.merge_element_count == 1:
                sort_text = TextMobject('Hier passiert \\\\ der "Sort"')
                sort_text.next_to(comp_text, DOWN)
                self.play(FadeInFromDown(sort_text))


            if left.values[left_l.get_value()] == 3:
                self.merge_runtime = 0.3
                dups_text = TextMobject('Links wird bei \\\\ Duplikaten bevorzugt')
                dups_text.next_to(comp_text, DOWN)
                sr = SurroundingRectangle(VGroup(*comp_text))
                self.play(
                    FadeIn(sr),
                    FadeInFromDown(dups_text),
                )
                self.wait()
                self.play(FadeOut(dups_text), FadeOut(sr))


            if left.values[left_l.get_value()] <= right.values[
                    right_r.get_value()]:
                self.play(CircleIndicate(lc), run_time=self.merge_runtime)

                lc = lc.copy()
                self.play(lc.move_to,
                          merged.elements[merged_m.get_value()],
                          run_time=self.merge_runtime)
                merged.elements.submobjects[merged_m.get_value()] = lc
                self.wait(duration=self.merge_runtime)
                self.play(*left_l.animate_set_index(left_l.get_value() + 1),
                          *merged_m.animate_set_index(merged_m.get_value() + 1),
                          run_time=self.merge_runtime)
                self.wait(duration=self.merge_runtime)
            else:
                self.play(CircleIndicate(rc), run_time=self.merge_runtime)

                rc = rc.copy()
                self.play(rc.move_to,
                          merged.elements[merged_m.get_value()],
                          run_time=self.merge_runtime)
                merged.elements.submobjects[merged_m.get_value()] = rc
                self.wait(duration=self.merge_runtime)
                self.play(*right_r.animate_set_index(right_r.get_value() + 1),
                          *merged_m.animate_set_index(merged_m.get_value() + 1),
                          run_time=self.merge_runtime)
                self.wait(duration=self.merge_runtime)
            if skip_to >= 2:
                break

        self.play(
            Uncreate(comp_text),
        )
        self.wait()

        cleanup_text = TextMobject('Links ist fertig ,\\\\also rechts beenden...')
        cleanup_text.next_to(merged, BOTTOM, SMALL_BUFF)


        self.play(
            FadeInFromDown(cleanup_text))
        self.wait()

        self.merge_runtime = 0.5

        while left_l.get_value() < len(left.values):
            self.animate_merge_element(left, left_l, merged, merged_m)
            if skip_to >= 3:
                break

        while right_r.get_value() < len(right.values):
            self.animate_merge_element(right, right_r, merged, merged_m)
            if skip_to >= 3:
                break

        self.play(Uncreate(left_l), Uncreate(right_r), Uncreate(merged_m),
                  Uncreate(cleanup_text))
        left.remove_index(left_l)
        right.remove(right_r)
        merged.remove_index(merged_m)


        t2 = TextMobject('Zwei Arrays von jeweils 4 zu einem 8 Array Zusammengeführt')
        t2.to_edge(UP)


        self.play(
            ReplacementTransform(t1, t2)
        )

        
        self.wait(duration=3)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()



class MergeBaseCase(MergeSortScenes):

    def construct(self):


        t1 = TextMobject(
            'Jetzt wissen wir, wie man \\\\ kleine Arrays, in ein Großes sortiert.'
        )
        self.play(FadeInFromDown(t1))
        self.wait(duration=3)

        t2 = TextMobject('Aber wie finden wir sortierte Arrays zum "Mergen"?')
        self.play(ReplacementTransform(t1, t2))
        self.wait(duration=2)

        t3 = TextMobject('Ein Array von 1 ist immer sortiert !')
        self.play(ReplacementTransform(t2, t3))
        self.wait()

        colors = [GREEN, YELLOW_D, PINK, BLUE]
        nums = [4, 12, 7]
        all_singles = VGroup(*[
            Array([n], show_labels=False, element_color=c)
            for n, c in zip(nums, colors)
        ])
        all_singles.arrange(RIGHT, buff=LARGE_BUFF * 3)
        all_taglines = VGroup(
            TextMobject('Dieses Array ist sortiert...'),
            TextMobject('... sowie dieses...'),
            TextMobject('... und auch das hier.'),
        )
        all_offsets = [UP, ORIGIN, DOWN]
        self.play(
            t3.to_edge,
            UP,
        )
        for a, t, o in zip(all_singles, all_taglines, all_offsets):
            a.shift(o)
            t.next_to(a, DOWN)
            self.play(
                ShowCreation(a),
                Write(t),
            )
        self.wait()

        t4 = TextMobject("Kommt einem etwas komisch vor,\\\\aber es ist wichtig !")
        all_singles[1].generate_target()
        all_singles[1].target.shift(UP)
        t4.next_to(all_singles[1].target, DOWN)
        self.play(
            FadeOut(all_singles[0]),
            FadeOut(all_taglines[0]),
            MoveToTarget(all_singles[1]),
            ReplacementTransform(all_taglines[1], t4),
            FadeOut(all_singles[2]),
            FadeOut(all_taglines[2]),
        )
        self.wait()

        t5 = TextMobject(
            r"Dies formt den ``\textbf{base case}'' für alle Merge Sorts.",
            tex_to_color_map={'base case': GREEN})
        t5.next_to(t4, DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(t5))
        self.wait(duration=2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class Merge4(MergeSortScenes):

    def construct(self):
        self.merge_runtime = 0.5

        colors = [RED, BLUE, GREEN, YELLOW_D]
        nums = [4, 3, 1, 7]
        all_singles = VGroup(*[
            Array([n], show_labels=False, element_color=c)
            for n, c in zip(nums, colors)
        ])
        all_singles.arrange(RIGHT, buff=0)
        t1 = TextMobject('Wir starten mit einem Array aus zufälligen Zahlen...')
        t1.to_edge(TOP)
        self.play(FadeInFromDown(t1), ShowCreation(all_singles))
        self.wait(duration=2)

        t2 = TextMobject('Und teilen es in viele 1-Element Arrays ')
        t2.to_edge(TOP)
        all_singles.generate_target(use_deepcopy=True)
        all_singles.target.arrange(RIGHT, buff=MED_LARGE_BUFF)
        self.play(
            ReplacementTransform(t1, t2),
            MoveToTarget(all_singles),
        )
        self.wait(duration=2)

        level_labels = [
            TextMobject('"Base cases"'),
            TextMobject('"Merged"'),
            TextMobject('Endergebnis')
        ]
        self.play(ReplacementTransform(t2, level_labels[0].to_edge(LEFT)))
        self.wait()

        self.play(
            VGroup(all_singles, level_labels[0]).to_edge, BOTTOM,
            {'buff': SMALL_BUFF})
        self.wait()

        current_level = all_singles
        all_levels = [current_level]
        while len(current_level) > 1:
            current_level = self.merge_level(current_level,
                                            0,
                                            buff=MED_LARGE_BUFF,
                                            speedy=True)
            ll = level_labels[len(all_levels)]
            ll.next_to(current_level, LEFT).to_edge(LEFT)
            self.play(Write(ll))
            self.wait()
            all_levels.append(current_level)

        g = VGroup(*all_levels, *level_labels)
        self.play(g.center)
        self.wait(duration=2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

    def setup_animate_merge(self, left, right, merged):
        show_labels = True
        if self.merge_current_level > 1:
            show_labels = False
        left_l = left.create_index(0,
                                color=YELLOW,
                                name='l',
                                show_label=show_labels)
        right_r = right.create_index(0,
                                    color=YELLOW,
                                    name='r',
                                    show_label=show_labels)
        merged_m = merged.create_index(0,
                                    color=YELLOW,
                                    name='m',
                                    position=UP,
                                    show_label=show_labels)
        self.play(FadeIn(left_l),
                FadeIn(right_r),
                FadeIn(merged_m),
                run_time=0.5)
        return left_l, right_r, merged_m

    def cleanup_animate_merge(self, left, left_l, right, right_r, merged,
                            merged_m):
        left.remove_index(left_l)
        right.remove(right_r)
        merged.remove_index(merged_m)
        self.play(FadeOut(left_l),
                FadeOut(right_r),
                FadeOut(merged_m),
                run_time=0.5)
        self.play(FadeOutAndShift(left, UP + RIGHT),
                FadeOutAndShift(right, UP + LEFT))



class Merge11(MergeSortScenes):

    def __init__(self, **kwargs):
        self.runtime_stack = []
        self.level_element_count = 0
        MergeSortScenes.__init__(self, **kwargs)

    def construct(self):
        n = 11

        t1 = TextMobject(
            'Jetzt ein etwas größerer "Merge" mit seltsamen Zahlen')
        self.play(FadeInFromDown(t1))
        self.wait()

        np.random.seed(42)
        colors = color_gradient([PINK, BLUE, YELLOW_D], 20)
        all_singles = VGroup(*[
            Array([n], show_labels=False, element_color=colors[n])
            for i, n in enumerate(np.random.randint(0, 20, n))
        ])
        all_singles.arrange(RIGHT, buff=MED_SMALL_BUFF)
        t2 = TextMobject(str(n) + " zahlen...")
        t2.next_to(all_singles, UP, buff=MED_LARGE_BUFF)
        self.play(FadeOutAndShift(t1, UP))
        self.play(ShowCreation(all_singles), FadeIn(t2))
        self.wait()

        b = BraceLabel(VGroup(*all_singles[-3:]),
                    'Schaut auf die letzten 3',
                    brace_direction=UP,
                    label_constructor=TextMobject)
        self.play(ShowCreation(b), FadeOutAndShift(t2, UP))
        self.wait()

        self.play(
            all_singles.to_edge,
            BOTTOM,
            {'buff': MED_SMALL_BUFF},

            FadeOutAndShift(b, UP))
        self.wait()

        current_level = all_singles
        all_levels = [current_level]
        squish_start_height = 14  # 4
        level_runtimes = [0.25, 0.25, 0.25, 0.25, 0.25]
        while len(current_level) > 1:
            if len(all_levels) == squish_start_height:
                g = VGroup(*all_levels[:-1])
                self.play(g.scale, 0.8, g.to_edge, BOTTOM, {'buff': SMALL_BUFF})
                self.play(all_levels[-1].next_to, all_levels[-2], UP,
                        {'buff': MED_SMALL_BUFF})
            if len(all_levels) > squish_start_height:
                self.play(all_levels[-2].scale, 0.8, all_levels[-2].next_to,
                        all_levels[-3], UP, {'buff': SMALL_BUFF})
                self.play(all_levels[-1].next_to, all_levels[-2], UP,
                        {'buff': SMALL_BUFF})

            self.level_element_count = 0
            self.merge_runtime = level_runtimes[self.merge_current_level]
            current_level = self.merge_level(current_level,
                                            len(all_levels),
                                            buff=MED_SMALL_BUFF,
                                            speedy=True)
            all_levels.append(current_level)

        merge_result = VGroup(*all_levels)
        self.play(merge_result.center)
        self.wait(duration=2)

        # In closing
        rt = TextMobject('Merge Sort - Part 1: Merging')
        rt.scale(1.5).to_edge(UP, buff=MED_SMALL_BUFF)

        one_element_array = all_levels[0][0]
        one_element_array.generate_target(use_deepcopy=True)
        oea_t = TextMobject('Ein 1-Element Array\\\\ist sortiert')
        oea_t.next_to(one_element_array.target, DOWN)
        oea_g = VGroup(one_element_array.target, oea_t)
        oea_g.next_to(rt, DOWN, buff=MED_LARGE_BUFF).to_edge(LEFT)

        two_to_four = VGroup(
            all_levels[1][0],
            all_levels[1][1],
            all_levels[2][0],
        )
        two_to_four.generate_target(use_deepcopy=True)
        ttf_t = TextMobject('Sortiert wird während des "merging"')
        ttf_t.next_to(two_to_four.target, DOWN)
        ttf_g = VGroup(two_to_four.target, ttf_t)
        ttf_g.next_to(rt, DOWN, buff=MED_LARGE_BUFF).to_edge(RIGHT)

        dups_from_left = VGroup(
            all_levels[3][0],
            all_levels[3][1],
            all_levels[4][0],
        )
        dups_from_left.generate_target(use_deepcopy=True)
        right_dup_fill_color = YELLOW
        dup_opacity = 0.2
        dups_from_left.target[1].backgrounds[1].set_fill(
            right_dup_fill_color, dup_opacity)
        dups_from_left.target[1].backgrounds[2].set_fill(
            right_dup_fill_color, dup_opacity)
        dups_from_left.target[2].backgrounds[4].set_fill(
            right_dup_fill_color, dup_opacity)
        dups_from_left.target[2].backgrounds[7].set_fill(
            right_dup_fill_color, dup_opacity)

        dfl_t = TextMobject(
            'Duplikate bevorzugen links - "merge" sort ist "stable"')
        dfl_t.next_to(dups_from_left.target, DOWN)
        dfl_g = VGroup(dups_from_left.target, dfl_t)
        dfl_g.next_to(VGroup(oea_g, ttf_g), DOWN, buff=LARGE_BUFF)

        self.play(
            FadeOut(merge_result),
            FadeInFromDown(rt),
            FadeInFromDown(oea_g),
            FadeInFromDown(ttf_g),
            FadeInFromDown(dfl_g),
        )
        self.wait(duration=5)

        end_scale_group = VGroup(*[
            mob for mob in self.mobjects if not isinstance(mob, ValueTracker)
        ])
        end_fade_group = VGroup()


    def setup_animate_merge(self, left, right, merged):
        left_l = left.create_index(0, color=YELLOW, name='l', show_label=False)
        right_r = right.create_index(0,
                                    color=YELLOW,
                                    name='r',
                                    show_label=False)
        merged_m = merged.create_index(0,
                                    color=YELLOW,
                                    name='m',
                                    position=UP,
                                    show_label=False)

        self.add(left_l, right_r, merged_m)
        return left_l, right_r, merged_m

    def cleanup_animate_merge(self, left, left_l, right, right_r, merged,
                            merged_m):
        left.remove_index(left_l)
        right.remove(right_r)
        merged.remove_index(merged_m)
        self.play(FadeOut(left_l),
                FadeOut(right_r),
                FadeOut(merged_m),
                FadeOutAndShift(left, UP + RIGHT),
                FadeOutAndShift(right, UP + LEFT),
                run_time=self.merge_runtime)

    def merge_level_pair_begin(self, index):
        if self.level_element_count == 0:
            self.runtime_stack.append(self.merge_runtime)


    def merge_level_pair_end(self, index):
        if self.level_element_count == 0:
            self.merge_runtime = self.runtime_stack.pop()
        self.level_element_count += 1
        self.merge_runtime *= 0.95

    def merge_level_extra_begin(self, index, extra):
        self.wait(duration=0.5)
        self.runtime_stack.append(self.merge_runtime)
        self.merge_runtime = 1
        self.play(ShowPassingFlashAround(extra))

        if self.merge_current_level == 1 or self.merge_current_level == 3:
            if self.merge_current_level == 1:
                pt = TextMobject('"promote" jedes\\\\nicht gepaarte Array')
            else:
                pt = TextMobject('wieder, "promote" das\\\\ungepaarte Array')
                pt.shift(UP * 2)
            pt.to_edge(RIGHT, buff=MED_SMALL_BUFF)
            a = Arrow(pt.get_bottom(), extra.get_top())
            self.play(FadeIn(pt), ShowCreation(a))
            self.wait()
            self.play(FadeOut(pt), FadeOut(a))

    def merge_level_extra_end(self, index, extra):

        self.merge_runtime = self.runtime_stack.pop()


class MergeNSpeedyClean(MergeSortScenes):

    def __init__(self, **kwargs):
        MergeSortScenes.__init__(self, **kwargs)

    def construct(self):
        n = 9
        np.random.seed(41)
        colors = color_gradient([PINK, BLUE, YELLOW_D], 20)
        all_singles = VGroup(*[
            Array([n], show_labels=False, element_color=colors[n])
            for i, n in enumerate(np.random.randint(0, 20, n))
        ])
        all_singles.arrange(RIGHT, buff=MED_SMALL_BUFF)
        all_singles.to_edge(BOTTOM, buff=SMALL_BUFF)
        self.play(ShowCreation(all_singles))

        current_level = all_singles
        all_levels = [current_level]
        self.merge_runtime = 0.5
        while len(current_level) > 1:
            current_level = self.merge_level(current_level,
                                            len(all_levels),
                                            buff=MED_SMALL_BUFF,
                                            speedy=True)
            all_levels.append(current_level)

        self.wait(duration=2)

    def setup_animate_merge(self, left, right, merged):
        left_l = left.create_index(0, color=YELLOW, show_label=False)
        right_r = right.create_index(0, color=YELLOW, show_label=False)
        merged_m = merged.create_index(0, color=YELLOW, show_label=False)
        self.add(left_l, right_r, merged_m)
        return left_l, right_r, merged_m

    def cleanup_animate_merge(self, left, left_l, right, right_r, merged,
                            merged_m):
        left.remove_index(left_l)
        right.remove(right_r)
        merged.remove_index(merged_m)
        self.play(FadeOut(left_l),
                FadeOut(right_r),
                FadeOut(merged_m),
                FadeOutAndShift(left, UP + RIGHT),
                FadeOutAndShift(right, UP + LEFT),
                run_time=self.merge_runtime)



class ArrayIndex(VGroup):
  
    

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
            self.show_arrow = False  
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
