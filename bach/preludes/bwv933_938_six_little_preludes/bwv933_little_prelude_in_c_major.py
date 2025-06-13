with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Prelude, BWV 933')
    with Identification():
        Creator('Johann Sebastian Bach', type='composer')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('http://musescore.com/user/27021897/scores/6356226')
    with Defaults():
        with Scaling():
            Millimeters(7.05556)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1683.36)
            PageWidth(1190.88)
            with PageMargins(type='even'):
                LeftMargin(56.6929)
                RightMargin(56.6929)
                TopMargin(56.6929)
                BottomMargin(113.386)
            with PageMargins(type='odd'):
                LeftMargin(56.6929)
                RightMargin(56.6929)
                TopMargin(56.6929)
                BottomMargin(113.386)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Prelude, BWV 933', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Sechs kleine Präludien', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=557.86):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(175.88)
                with StaffLayout(number=2):
                    StaffDistance(83.35)
            with Attributes():
                Divisions(40.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-41.11, default_y=32.68, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('88')
                Staff(1)
                Sound(tempo=88.0)
            with Direction():
                with DirectionType():
                    Words('Allegro moderato, un poco pomposo', relative_x=-97.39, relative_y=30.88)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-71.95, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=87.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=108.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=129.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=275.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('4')
            with Note(default_x=321.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=342.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=363.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=510.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(160.0)
            with Note(default_x=87.48, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=87.48, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(20.0)
            with Note(default_x=275.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('¨2', placement='below')
            with Note(default_x=321.87, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=321.87, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(20.0)
            with Note(default_x=510.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(160.0)
            with Note():
                Rest()
                Duration(10.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('marcato, quasi non legato', default_y=-50.16, relative_x=-52.75, relative_y=-55.18, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=129.33, default_y=-183.35):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=162.82, default_y=-173.35):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=196.3, default_y=-163.35):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=229.79, default_y=-148.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note():
                Rest()
                Duration(10.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=363.73, default_y=-183.35):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=397.21, default_y=-173.35):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=430.69, default_y=-163.35):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=464.18, default_y=-148.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
        with Measure(number='2', width=498.63):
            with Note(default_x=11.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('3')
            with Note(default_x=29.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=48.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=78.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2')
            with Note(default_x=138.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=197.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('3')
            with Note(default_x=257.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('4')
            with Note(default_x=317.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(160.0)
            with Note(default_x=11.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=78.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=197.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=257.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=317.59, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest()
                Duration(10.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=48.44, default_y=-148.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=78.35, default_y=-143.35):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.25, default_y=-148.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=138.16, default_y=-153.35):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=168.06, default_y=-143.35):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=197.97, default_y=-163.35):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=227.88, default_y=-153.35):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=257.78, default_y=-148.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=287.69, default_y=-183.35):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=317.59, default_y=-173.35):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=347.5, default_y=-163.35):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=377.41, default_y=-148.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=407.31, default_y=-143.35):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=437.22, default_y=-138.35):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=467.13, default_y=-133.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=533.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(114.57)
                with StaffLayout(number=2):
                    StaffDistance(111.5)
            with Note(default_x=64.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('3')
            with Note(default_x=87.37, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=110.16, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=239.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('3')
            with Note(default_x=277.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('3')
            with Note(default_x=297.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=318.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=349.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=369.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='stop')
                    with Technical():
                        Fingering('3')
            with Note(default_x=395.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=2)
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=493.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('4')
            with Backup():
                Duration(160.0)
            with Note(default_x=64.11, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Forward():
                Duration(20.0)
            with Note(default_x=239.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=277.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(20.0)
            with Note(default_x=493.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=3)
                    with Technical():
                        Fingering('2', placement='below')
            with Backup():
                Duration(160.0)
            with Note(default_x=64.11, default_y=-156.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=110.16, default_y=-191.5):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=140.57, default_y=-181.5):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=170.97, default_y=-171.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=201.38, default_y=-156.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note():
                Rest()
                Duration(10.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=333.76, default_y=-191.5):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=395.03, default_y=-181.5):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=425.44, default_y=-171.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=455.84, default_y=-156.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
        with Measure(number='4', width=522.99):
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('3')
            with Note(default_x=69.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('4')
            with Note(default_x=125.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=152.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=180.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=208.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('5')
            with Note(default_x=236.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('4')
            with Note(default_x=264.02, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Technical():
                        Fingering('3')
            with Note(default_x=287.72, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=306.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=337.64, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=357.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='stop')
                    with Technical():
                        Fingering('3')
            with Note(default_x=382.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('più leggiero', default_y=-40.0, relative_x=11.16, relative_y=-59.1, font_style='italic', font_size='11')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.53, default_y=-41.21, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(10.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-76.21)
                Staff(1)
            with Note(default_x=437.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=465.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=493.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(160.0)
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=3)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=69.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=125.01, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=180.62, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=236.22, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=264.02, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1', placement='below')
            with Backup():
                Duration(120.0)
            with Note():
                Rest()
                Duration(10.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=41.6, default_y=-191.5):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=69.41, default_y=-176.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.21, default_y=-166.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=125.01, default_y=-201.5):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=180.62, default_y=-196.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=236.22, default_y=-191.5):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=264.02, default_y=-156.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=321.97, default_y=-171.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=382.38, default_y=-181.5):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=410.18, default_y=-191.5):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=465.78, default_y=-156.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='5', width=553.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.63)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=61.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=92.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=122.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=214.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=245.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.17, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=306.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=337.54, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=368.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=429.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=460.28, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=490.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=521.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Backup():
                Duration(160.0)
            with Note():
                Rest(measure='yes')
                Duration(160.0)
                Voice('2')
                Staff(1)
            with Backup():
                Duration(160.0)
            with Note(default_x=61.37, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=122.74, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=184.11, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=245.48, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=306.85, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=368.22, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=429.59, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=490.96, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
        with Measure(number='6', width=502.56):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=40.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=132.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=163.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=194.11, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=255.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=286.17, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=347.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=378.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=408.91, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=439.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=470.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(160.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=71.37, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=132.74, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=194.11, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=255.48, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=316.85, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=378.22, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=439.59, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
        with Measure(number='7', width=401.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.63)
                with StaffLayout(number=2):
                    StaffDistance(96.46)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-83.43)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-83.43)
                Staff(1)
            with Note(default_x=61.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=81.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=102.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=122.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=152.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=172.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=213.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=233.99, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=254.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=315.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=335.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=356.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=376.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(160.0)
            with Note(default_x=61.37, default_y=-171.46):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=102.15, default_y=-141.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=152.44, default_y=-171.46):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=193.22, default_y=-141.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=233.99, default_y=-146.46):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=274.77, default_y=-136.46):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=315.55, default_y=-146.46):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=356.33, default_y=-156.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('4', placement='below')
        with Measure(number='8', width=277.45):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.43, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        StrongAccent(type='up')
                    with Technical():
                        Fingering('5')
            with Note(default_x=38.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-85.79)
                Staff(1)
            with Note(default_x=66.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('4')
            with Note(default_x=83.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=101.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=131.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=148.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
                    with Technical():
                        Fingering('5')
            with Note(default_x=166.03, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.79, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=185.5, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(160.0)
            with Note(default_x=10.0, default_y=-166.46):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=38.03, default_y=-151.46):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=66.06, default_y=-161.46):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=101.1, default_y=-156.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=148.52, default_y=-141.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('1', placement='below')
            with Note():
                Rest()
                Duration(10.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=203.02, default_y=-141.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=220.54, default_y=-176.46):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=377.56):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-79.95, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=35.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('5')
            with Note(print_object='no'):
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=179.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('4')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-85.06, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=213.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=343.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(160.0)
            with Note(default_x=31.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(5.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=69.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(5.0)
                Voice('2')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=85.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('3', placement='below')
            with Forward():
                Duration(20.0)
            with Note(default_x=179.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=209.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(5.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=233.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(5.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=249.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('3', placement='below')
            with Forward():
                Duration(20.0)
            with Note(default_x=343.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('1', placement='below')
            with Backup():
                Duration(160.0)
            with Note(default_x=35.64, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('3')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(40.0)
            with Note(default_x=213.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('3')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest()
                Duration(10.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=85.5, default_y=-176.46):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=107.01, default_y=-166.46):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=128.52, default_y=-156.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=3)
                    with Articulations():
                        Staccato()
            with Note(default_x=150.02, default_y=-141.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note():
                Rest()
                Duration(10.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=249.1, default_y=-176.46):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
            with Note(default_x=270.6, default_y=-166.46):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.11, default_y=-156.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=3)
                    with Articulations():
                        Staccato()
            with Note(default_x=313.61, default_y=-141.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
        with Measure(number='10', width=546.15):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.67)
                with StaffLayout(number=2):
                    StaffDistance(94.59)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.92, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=69.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('4')
            with Note(default_x=128.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=188.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=247.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=306.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('4')
            with Note(default_x=366.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(160.0)
            with Note(default_x=69.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=128.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=188.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=247.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=306.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=366.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(120.0)
            with Note():
                Rest()
                Duration(10.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=98.81, default_y=-134.59):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=128.51, default_y=-129.59):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=158.22, default_y=-134.59):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=188.11, default_y=-139.59):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=217.82, default_y=-129.59):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.52, default_y=-149.59):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.22, default_y=-139.59):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=306.92, default_y=-134.59):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=336.63, default_y=-169.59):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=366.33, default_y=-159.59):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=396.03, default_y=-149.59):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2', placement='below')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=425.73, default_y=-134.59):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=455.44, default_y=-129.59):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=485.14, default_y=-124.59):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=514.84, default_y=-119.59):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='11', width=510.35):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.2, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=16.09, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('5')
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=192.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('4')
            with Note(default_x=237.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('3')
            with Note(default_x=258.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=278.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('3')
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=443.06, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('5')
            with Backup():
                Duration(160.0)
            with Note(default_x=16.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Forward():
                Duration(20.0)
            with Note(default_x=192.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=237.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(20.0)
            with Note(default_x=443.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('1', placement='below')
            with Backup():
                Duration(160.0)
            with Note(default_x=20.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(40.0)
            with Note(default_x=16.09, default_y=-114.59):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=48.93, default_y=-149.59):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=81.78, default_y=-139.59):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=114.62, default_y=-124.59):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=147.47, default_y=-114.59):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
                    with Technical():
                        Fingering('1', placement='below')
            with Note():
                Rest()
                Duration(10.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=278.84, default_y=-144.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=311.68, default_y=-134.59):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=344.53, default_y=-124.59):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=377.37, default_y=-109.59):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=410.22, default_y=-114.59):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=443.06, default_y=-109.59):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=475.9, default_y=-114.59):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3', placement='below')
        with Measure(number='12', width=605.67):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(79.43)
                with StaffLayout(number=2):
                    StaffDistance(95.96)
            with Note(default_x=72.91, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('4')
            with Note(default_x=137.29, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-84.74)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-84.74)
                Staff(1)
            with Note(default_x=201.67, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('4')
            with Note(default_x=266.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('3')
            with Note(default_x=330.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('4')
            with Note(default_x=350.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=370.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=390.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Note(default_x=410.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.53, default_y=-41.2, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-76.2)
                Staff(1)
            with Note():
                Rest()
                Duration(10.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=507.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=539.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=571.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(160.0)
            with Note(default_x=72.91, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=137.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=201.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=266.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=330.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=410.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('1', placement='below')
            with Backup():
                Duration(120.0)
            with Note(default_x=72.91, default_y=-120.96):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=105.1, default_y=-125.96):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=137.29, default_y=-120.96):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=169.48, default_y=-125.96):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=201.67, default_y=-130.96):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=233.87, default_y=-140.96):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=266.06, default_y=-125.96):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=298.25, default_y=-115.96):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=330.44, default_y=-105.96):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=370.68, default_y=-110.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=410.92, default_y=-105.96):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=443.11, default_y=-120.96):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=475.3, default_y=-130.96):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=507.49, default_y=-120.96):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=539.68, default_y=-140.96):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=571.87, default_y=-130.96):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='13', width=450.83):
            with Direction(placement='below'):
                with DirectionType():
                    Words('più leggiero e', default_y=-40.0, relative_x=-11.16, relative_y=-38.68, font_style='italic', font_size='11')
                Staff(1)
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=37.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=64.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=119.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=148.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=175.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=230.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=257.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=339.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=367.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=394.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=421.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Backup():
                Duration(160.0)
            with Note(default_x=10.0, default_y=-150.96):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=64.72, default_y=-125.96):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=119.43, default_y=-150.96):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=175.65, default_y=-125.96):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=230.37, default_y=-145.96):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=285.08, default_y=-125.96):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=339.8, default_y=-150.96):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=394.51, default_y=-125.96):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
        with Measure(number='14', width=420.58):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(88.04)
            with Note(default_x=61.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=83.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=153.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=175.97, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=197.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=241.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=263.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=329.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=351.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=373.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=395.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Backup():
                Duration(160.0)
            with Note(default_x=61.37, default_y=-148.04):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=105.34, default_y=-123.04):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=153.99, default_y=-153.04):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=197.96, default_y=-128.04):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
            with Note(default_x=241.93, default_y=-158.04):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=285.89, default_y=-138.04):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=329.86, default_y=-143.04):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=373.83, default_y=-148.04):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('4', placement='below')
        with Measure(number='15', width=356.01):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=31.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=95.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=117.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=138.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=181.33, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=202.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=224.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=245.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=266.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=288.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=309.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=331.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(160.0)
            with Note(default_x=10.0, default_y=-153.04):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=52.83, default_y=-143.04):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=95.66, default_y=-138.04):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=138.5, default_y=-128.04):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=181.33, default_y=-138.04):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=224.16, default_y=-148.04):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=266.99, default_y=-133.04):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=309.83, default_y=-138.04):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('2', placement='below')
        with Measure(number='16', width=279.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=11.48, relative_y=-45.74):
                        Fff()
                Staff(1)
                Sound(dynamics=140.0)
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        StrongAccent(type='up')
                    with Technical():
                        Fingering('5')
            with Note(default_x=40.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=70.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('4')
            with Note(default_x=88.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=126.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=145.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
                    with Technical():
                        Fingering('5')
            with Note(default_x=163.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=182.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=201.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(160.0)
            with Note(default_x=10.0, default_y=-143.04):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=40.03, default_y=-128.04):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=70.07, default_y=-138.04):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        DetachedLegato()
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=107.61, default_y=-133.04):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                        Staccatissimo()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=145.16, default_y=-153.04):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        DetachedLegato()
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=220.24, default_y=-188.04):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        DetachedLegato()
                    with Technical():
                        Fingering('5', placement='below')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Fermata(None, type='upright', relative_y=10.0)
                Repeat(direction='backward')