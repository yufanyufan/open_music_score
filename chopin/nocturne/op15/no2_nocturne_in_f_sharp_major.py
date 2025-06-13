with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Nocturne Op. 15 No. 2 in F♯ major')
    with Identification():
        Creator('Frédéric Chopin', type='composer')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(7.056)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2381.64)
            PageWidth(1683.28)
            with PageMargins(type='even'):
                LeftMargin(56.6894)
                RightMargin(56.6894)
                TopMargin(56.6894)
                BottomMargin(113.379)
            with PageMargins(type='odd'):
                LeftMargin(56.6894)
                RightMargin(56.6894)
                TopMargin(56.6894)
                BottomMargin(113.379)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Nocturne Op. 15 No. 2 in F♯ major', default_x=841.641, default_y=2293.77, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Frédéric Chopin', default_x=1626.59, default_y=2224.95, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('鋼琴')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('鋼琴')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=240.02):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(176.22)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(240.0)
                with Key():
                    Fifths(6)
                with Time():
                    Beats('2')
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
                    Words('Larghetto', default_x=-36.12, default_y=25.68, relative_y=20.0, font_weight='bold', font_size='13')
                Staff(1)
                Sound(tempo=40.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='yes', default_x=-36.12, relative_x=122.87, relative_y=49.02):
                        BeatUnit('quarter')
                        PerMinute('40')
                Staff(1)
                Sound(tempo=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('sostenuto', default_y=-46.15, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=152.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=209.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(120.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='1', width=295.75):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-51.92)
                Staff(1)
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=52.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.8, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=130.61, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-49.15)
                Staff(1)
            with Note(default_x=169.55, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=231.85, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.01)
                Staff(2)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.68, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.55, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.55, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=231.85, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='2', width=330.69):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=74.91, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=130.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=158.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=186.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=247.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=301.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.01)
                Staff(2)
            with Note(default_x=13.8, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=74.91, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.01, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.01, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=247.12, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='3', width=334.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.25, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=23.49, relative_x=7.37)
                Staff(1)
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=52.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=28.26)
                Staff(1)
            with Note(default_x=178.3, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-48.46, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=217.01, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=274.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.01)
                Staff(2)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=115.4, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=217.01, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=217.01, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=274.9, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='4', width=348.05):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=74.46, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=99.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
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
            with Note(default_x=125.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
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
            with Note(default_x=150.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
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
            with Note(default_x=175.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=201.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=261.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=316.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.01)
                Staff(2)
            with Note(default_x=13.8, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=74.46, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=201.2, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=201.2, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=201.2, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='5', width=332.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(143.08)
                with StaffLayout(number=2):
                    StaffDistance(89.49)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-51.92)
                Staff(1)
            with Note(default_x=135.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=161.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=192.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-49.15)
                Staff(1)
            with Note(default_x=245.33, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=287.89, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.01)
                Staff(2)
            with Note(default_x=135.01, default_y=-184.49):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=192.14, default_y=-149.49):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=245.33, default_y=-139.49):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=245.33, default_y=-119.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=287.89, default_y=-149.49):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='6', width=272.92):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=68.07, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=126.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=162.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(480.0)
            with Note(default_x=10.0, default_y=-169.49):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=68.07, default_y=-149.49):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=68.07, default_y=-134.49):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=68.07, default_y=-124.49):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=126.14, default_y=-159.49):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=198.73, default_y=-149.49):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=198.73, default_y=-134.49):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=198.73, default_y=-114.49):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='7', width=315.56):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=74.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=127.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=154.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=192.6, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=203.57, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=215.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note():
                Rest()
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Staff(1)
            with Note(default_x=286.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-134.49):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-114.49):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.1, default_y=-114.49):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=154.98, default_y=-124.49):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=215.28, default_y=-119.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=286.55, default_y=-124.49):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-154.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=215.28, default_y=-154.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(90.0)
                Tie(type='stop')
                Voice('6')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=286.55, default_y=-154.49):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(30.0)
                Voice('6')
                Type('32nd')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(120.0)
            with Note(default_x=79.1, default_y=-139.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=225.28, default_y=-144.49):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='8', width=352.09):
            with Note(default_x=26.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=77.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=122.13, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=145.19, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=145.19, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-72.98, relative_x=13.52)
                Staff(1)
            with Note(default_x=197.9, default_y=-60.0, print_object='no'):
                Cue()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=226.7, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=24.88, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('40')
                Staff(1)
                Sound(tempo=40.0)
            with Note(default_x=282.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=327.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-1.23)
                Staff(1)
            with Backup():
                Duration(600.0)
            with Forward():
                Duration(360.0)
            with Note(default_x=193.61, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(600.0)
            with Note(default_x=26.4, default_y=-149.49):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=26.4, default_y=-129.49):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=8.77, relative_x=8.6)
                Staff(2)
            with Note(default_x=77.14, default_y=-159.49):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=77.14, default_y=-129.49):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none', relative_x=14.74)
                Staff(2)
            with Note(default_x=145.19, default_y=-154.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=145.19, default_y=-144.49):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=195.92, default_y=-174.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Note(default_x=195.92, default_y=-154.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Note(default_x=195.92, default_y=-139.49):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Note(default_x=282.34, default_y=-174.49, print_object='no'):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=282.34, default_y=-154.49, print_object='no'):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=282.34, default_y=-139.49, print_object='no'):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(600.0)
            with Note(default_x=30.7, default_y=-139.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(360.0)
        with Measure(number='9', width=276.29):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=25.73, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Staff(1)
                Sound(tempo=70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=4.61, default_y=-74.06, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=19.88, default_y=-55.0, print_object='no'):
                Cue()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=47.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=22.98, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('40')
                Staff(1)
                Sound(tempo=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-54.11)
                Staff(1)
            with Note(default_x=73.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=101.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.46, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-3.69)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-48.83, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=185.37, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=230.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(600.0)
            with Note(default_x=15.6, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(60.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.01)
                Staff(2)
            with Note(default_x=73.73, default_y=-189.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=129.55, default_y=-154.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.37, default_y=-144.49):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.37, default_y=-124.49):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=230.03, default_y=-154.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='10', width=670.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(143.08)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=135.01, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.35)
                Staff(1)
            with Note(default_x=212.93, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=256.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=299.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=342.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=385.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-101.98)
                Staff(1)
            with Note(default_x=463.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=492.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=521.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=552.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=580.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=609.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=639.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.5)
                Staff(2)
            with Note(default_x=135.01, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=212.93, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=385.66, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=385.66, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=463.58, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='11', width=878.56):
            with Direction(placement='above'):
                with DirectionType():
                    Words('leggiero', default_y=49.11, relative_y=-35.0, font_style='italic', font_size='9')
                Staff(1)
            with Note(default_x=9.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=37.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=94.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=123.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=151.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=208.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=244.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=273.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=301.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=330.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=358.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=387.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=415.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=444.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=472.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=501.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=529.69, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=558.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=586.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=615.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=643.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=679.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=707.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=736.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=764.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=793.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=821.91, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=850.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.5)
                Staff(2)
            with Note(default_x=7.41, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=224.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=442.18, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=442.18, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=659.57, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(120.0)
            with Note(default_x=224.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(120.0)
        with Measure(number='12', width=598.88):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(129.05)
                with StaffLayout(number=2):
                    StaffDistance(80.2)
            with Note(default_x=131.21, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=149.65, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=207.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=238.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=269.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=301.07, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
            with Note(default_x=351.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('backward hook', number=4)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=371.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-83.66)
                Staff(1)
            with Note(default_x=429.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=457.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=485.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-48.66, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=513.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=541.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=569.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=149.65, default_y=-165.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=207.81, default_y=-145.2):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=371.01, default_y=-130.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=371.01, default_y=-120.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=371.01, default_y=-110.2):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='13', width=499.3):
            with Note(default_x=14.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    with Articulations():
                        Staccato()
            with Note(default_x=56.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=98.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=154.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=197.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=239.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=295.15, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=327.76, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=362.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=386.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=425.29, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural-sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=449.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=473.56, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=14.0, default_y=-175.2):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=126.8, default_y=-140.2):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=239.59, default_y=-130.2):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=239.59, default_y=-110.2):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=327.76, default_y=-140.2):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='14', width=450.72):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=48.07, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=86.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=35.7, relative_y=30.0):
                        OtherDynamics('con forza')
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=124.2, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=184.89, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(30.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=217.04, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=249.18, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=281.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=313.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=345.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=377.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=401.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=425.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=10.0, default_y=-160.2):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=124.2, default_y=-140.2):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=124.2, default_y=-125.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=124.2, default_y=-115.2):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=173.03, default_y=-130.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.89, default_y=-125.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=184.89, default_y=-115.2):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=184.89, default_y=-105.2):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=313.46, default_y=-125.2):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=313.46, default_y=-115.2):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=313.46, default_y=-105.2):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=313.46, default_y=-95.2):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='15', width=502.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(143.08)
                with StaffLayout(number=2):
                    StaffDistance(101.93)
            with Note(default_x=135.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=208.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=273.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=307.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=357.94, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=368.9, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=380.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Staff(1)
            with Note(default_x=467.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-130.49)
                Staff(2)
            with Note(default_x=134.65, default_y=-166.93):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none', relative_x=39.32)
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(default_x=135.01, default_y=-201.93):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=208.52, default_y=-151.93):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=380.62, default_y=-156.93):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(120.0)
            with Note(default_x=208.52, default_y=-126.93):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=307.11, default_y=-136.93):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('7')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=380.62, default_y=-131.93):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('7')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(30.0)
                Voice('7')
                Type('32nd')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=11.47, relative_x=18.43)
                Staff(2)
            with Note(default_x=467.49, default_y=-136.93):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(30.0)
                Voice('7')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='16', width=297.65):
            with Note(default_x=30.2, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=30.2, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('natural-sharp')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=213.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=268.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(480.0)
            with Note(default_x=30.2, default_y=-186.93):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=91.44, default_y=-141.93):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=91.44, default_y=-131.93):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=152.67, default_y=-151.93):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=152.67, default_y=-141.93):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='17', width=312.14):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.4, relative_y=-45.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-80.4)
                Staff(1)
            with Note(default_x=82.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=173.84, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=242.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-19.63, relative_y=-27.73):
                        Fz()
                Staff(2)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.22)
                Staff(2)
            with Note(default_x=13.8, default_y=-201.93):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=82.15, default_y=-146.93):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=82.15, default_y=-131.93):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=82.15, default_y=-121.93):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=173.84, default_y=-156.93):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=173.84, default_y=-146.93):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=173.84, default_y=-131.93):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=242.19, default_y=-146.93):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=242.19, default_y=-131.93):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=242.19, default_y=-121.93):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='18', width=436.61):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-45.4, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Accent()
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-6.14)
                Staff(1)
            with Note(default_x=283.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(120.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('dolciss.', relative_x=50.38, relative_y=40.89, font_style='italic', font_size='9')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=32.54, relative_x=66.35)
                Staff(1)
            with Note(default_x=142.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(17.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=160.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(17.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(17.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=201.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(17.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=221.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(17.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=239.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(17.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=257.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(17.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(240.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-63.9)
                Staff(2)
            with Note(default_x=10.0, default_y=-166.93):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=165.53, default_y=-141.93):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=165.53, default_y=-131.93):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=165.53, default_y=-116.93):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=283.96, default_y=-151.93):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=283.96, default_y=-141.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=283.96, default_y=-131.93):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=359.49, default_y=-141.93):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=359.49, default_y=-131.93):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=359.49, default_y=-116.93):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='19', width=539.46):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(143.08)
                with StaffLayout(number=2):
                    StaffDistance(108.54)
            with Note(default_x=135.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=213.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=282.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=317.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=383.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=472.21, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.1)
                Staff(2)
            with Note(default_x=135.01, default_y=-208.54):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=135.01, default_y=-173.54):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=213.12, default_y=-148.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=213.12, default_y=-138.54):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=213.12, default_y=-123.54):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=317.88, default_y=-158.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=317.88, default_y=-148.54):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=317.88, default_y=-138.54):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=427.87, default_y=-148.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=427.87, default_y=-138.54):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=427.87, default_y=-113.54):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='20', width=565.84):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_y=-40.0):
                        Pp()
                        OtherDynamics(' e poco riten.')
                Staff(1)
                Sound(dynamics=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=24.34, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('36')
                Staff(1)
                Sound(tempo=36.0)
            with Note(default_x=17.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=377.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(120.0)
            with Note(default_x=183.07, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(15.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=206.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=229.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=253.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=276.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=299.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=322.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=346.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(1)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(240.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.1)
                Staff(2)
            with Note(default_x=17.8, default_y=-208.54):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=17.8, default_y=-173.54):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=226.09, default_y=-148.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=226.09, default_y=-133.54):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=226.09, default_y=-123.54):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=377.65, default_y=-158.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=377.65, default_y=-148.54):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=377.65, default_y=-133.54):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=470.94, default_y=-148.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=470.94, default_y=-133.54):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=470.94, default_y=-123.54):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='21', width=443.61):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-78.62)
                Staff(1)
            with Note(default_x=105.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=186.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=227.91, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-99.66, relative_x=1.23)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-99.66, relative_x=1.23)
                Staff(1)
            with Note(default_x=319.35, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=400.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.1)
                Staff(2)
            with Note(default_x=13.8, default_y=-213.54):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-178.54):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=105.25, default_y=-148.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=105.25, default_y=-133.54):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=105.25, default_y=-123.54):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=227.91, default_y=-158.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=227.91, default_y=-148.54):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=227.91, default_y=-133.54):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=319.35, default_y=-153.54):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=319.35, default_y=-118.54):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='22', width=586.9):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(116.28)
                with StaffLayout(number=2):
                    StaffDistance(77.55)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=147.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(180.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=282.89, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=338.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=379.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=420.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=461.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=503.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=544.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.1)
                Staff(2)
            with Note(default_x=147.05, default_y=-187.55):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=147.05, default_y=-152.55):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=227.31, default_y=-132.55):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-43.78, default_y=40.51)
            with Note(default_x=227.31, default_y=-117.55):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-43.78, default_y=40.51)
            with Note(default_x=227.31, default_y=-107.55):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-43.78, default_y=40.51)
            with Note(default_x=227.31, default_y=-82.55):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-43.78, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=72.49)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.1)
                Staff(2)
            with Note(default_x=338.47, default_y=-187.55):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=338.47, default_y=-152.55):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=461.88, default_y=-132.55):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.75, default_y=35.51)
            with Note(default_x=461.88, default_y=-112.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.75, default_y=35.51)
            with Note(default_x=461.88, default_y=-102.55):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.75, default_y=35.51)
            with Note(default_x=461.88, default_y=-87.55):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.75, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=86.01)
                Staff(2)
        with Measure(number='23', width=484.27):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(180.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=142.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=196.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=241.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('natural-sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=329.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=360.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=390.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=421.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=452.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.1)
                Staff(2)
            with Note(default_x=13.8, default_y=-187.55):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-152.55):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=87.11, default_y=-132.55):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.75, default_y=40.51)
            with Note(default_x=87.11, default_y=-107.55):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.75, default_y=40.51)
            with Note(default_x=87.11, default_y=-82.55):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.75, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=77.41)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.1)
                Staff(2)
            with Note(default_x=196.97, default_y=-187.55):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=196.97, default_y=-152.55):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=329.5, default_y=-137.55):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.95, default_y=30.51)
            with Note(default_x=329.5, default_y=-122.55):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.95, default_y=30.51)
            with Note(default_x=329.5, default_y=-92.55):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.95, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=122.87)
                Staff(2)
        with Measure(number='24', width=477.74):
            with Direction(placement='below'):
                with DirectionType():
                    Words('string.', default_y=-40.0, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=130.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Words('riten.', default_y=-67.32, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=1.7, relative_x=-44.23, relative_y=37.72):
                        BeatUnit('quarter')
                        PerMinute('32')
                Staff(1)
                Sound(tempo=32.0)
            with Note(default_x=245.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.31, relative_x=-27.03, relative_y=31.23):
                        BeatUnit('quarter')
                        PerMinute('28')
                Staff(1)
                Sound(tempo=28.0)
            with Note(default_x=284.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=2.9, relative_x=-6.14, relative_y=34.86):
                        BeatUnit('quarter')
                        PerMinute('24')
                Staff(1)
                Sound(tempo=24.0)
            with Note(default_x=322.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=2.5, relative_x=-1.23, relative_y=27.89):
                        BeatUnit('quarter')
                        PerMinute('20')
                Staff(1)
                Sound(tempo=20.0)
            with Note(default_x=361.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=31.28, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('16')
                Staff(1)
                Sound(tempo=16.0)
            with Note(default_x=399.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=23.5, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('10')
                Staff(1)
                Sound(tempo=10.0)
            with Note(default_x=437.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.1)
                Staff(2)
            with Note(default_x=13.8, default_y=-187.55):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=53.96, default_y=-142.55):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.34, default_y=-117.55):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.72, default_y=-132.55):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.1, default_y=-107.55):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=11.23, relative_x=7.37)
                Staff(2)
            with Note(default_x=207.48, default_y=-117.55):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none', relative_x=6.14)
                Staff(2)
            with Note(default_x=245.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
        with Measure(number='25', width=596.82):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(99.19)
                with StaffLayout(number=2):
                    StaffDistance(98.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Doppio movimento', default_y=61.19, relative_y=20.0, font_weight='bold', font_size='13')
                Staff(1)
                Sound(tempo=80.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('sotto voce', default_y=-63.6, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-56.2, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=156.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=333.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-103.66)
                Staff(1)
            with Note(default_x=375.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=553.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note(default_x=156.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=198.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.1, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=375.72, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=417.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=459.34, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=511.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=553.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=198.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=239.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=417.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=459.34, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=292.1, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=375.72, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=511.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-95.49)
                Staff(2)
            with Note(default_x=156.22, default_y=-198.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural-sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=265.97, default_y=-163.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=265.97, default_y=-143.67):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=265.97, default_y=-133.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=485.47, default_y=-178.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='26', width=455.1):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=191.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=233.65, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=411.63, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=55.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=233.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=275.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=370.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.63, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=55.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=97.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=275.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=317.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=149.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=233.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=369.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-198.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=123.73, default_y=-163.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=123.73, default_y=-143.67):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=123.73, default_y=-133.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=343.58, default_y=-178.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='27', width=496.98):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-56.3, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=53.08)
                Staff(1)
            with Note(default_x=13.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=3.69)
                Staff(1)
            with Note(default_x=208.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=47.35)
                Staff(1)
            with Note(default_x=254.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-2.46)
                Staff(1)
            with Note(default_x=449.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=59.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=254.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=300.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=403.65, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=449.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=59.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=105.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=300.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=346.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=162.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=254.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=403.65, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-198.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=134.19, default_y=-163.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=374.98, default_y=-198.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(120.0)
            with Note(default_x=134.19, default_y=-143.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=134.19, default_y=-133.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-95.49)
                Staff(2)
            with Note(default_x=254.59, default_y=-143.67):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=254.59, default_y=-133.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(120.0)
        with Measure(number='28', width=594.75):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(119.77)
            with Note(default_x=152.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Backup():
                Duration(480.0)
            with Note(default_x=152.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=194.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-80.56)
                Staff(1)
            with Note(default_x=236.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=288.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-48.7, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=372.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=414.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=456.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=509.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=551.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=288.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=372.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(384.0)
            with Note(default_x=164.75, default_y=-164.77):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-19.71, relative_x=1.23)
                Staff(2)
            with Note(default_x=262.6, default_y=-159.77):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=1.23)
                Staff(2)
            with Note(default_x=372.78, default_y=-164.77):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=482.97, default_y=-199.77):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(480.0)
            with Note(default_x=152.42, default_y=-184.77):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=152.42, default_y=-149.77):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Forward():
                Duration(120.0)
        with Measure(number='29', width=471.79):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=198.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-103.66)
                Staff(1)
            with Note(default_x=242.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=426.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=57.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=100.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=242.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=285.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=383.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=426.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=57.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=100.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=285.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=328.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=155.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=242.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=383.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-103.09)
                Staff(2)
            with Note(default_x=13.8, default_y=-219.77):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=127.9, default_y=-184.77):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=127.9, default_y=-164.77):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=127.9, default_y=-154.77):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=356.09, default_y=-199.77):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='30', width=482.36):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=202.81, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=247.28, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=436.29, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=58.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.81, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=247.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=291.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=391.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=436.29, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=58.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=102.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=291.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=336.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=158.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=247.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=391.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-219.77):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=130.54, default_y=-184.77):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=130.54, default_y=-164.77):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=130.54, default_y=-154.77):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=364.02, default_y=-199.77):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='31', width=586.85):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(101.08)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-56.3, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=50.72)
                Staff(1)
            with Note(default_x=135.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=3.69)
                Staff(1)
            with Note(default_x=317.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=45.0)
                Staff(1)
            with Note(default_x=360.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-2.46)
                Staff(1)
            with Note(default_x=542.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=135.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=177.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-90.3)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-90.3)
                Staff(1)
            with Note(default_x=220.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=360.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=403.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=445.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=499.49, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=542.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=177.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=220.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=403.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=445.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=135.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=274.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=360.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=499.49, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=135.01, default_y=-201.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=247.57, default_y=-166.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-95.49)
                Staff(2)
            with Note(default_x=472.69, default_y=-201.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=74.95)
                Staff(2)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(120.0)
            with Note(default_x=247.57, default_y=-146.08):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=247.57, default_y=-136.08):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=360.13, default_y=-146.08):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=360.13, default_y=-136.08):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(120.0)
        with Measure(number='32', width=476.75):
            with Note(default_x=30.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=210.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=252.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-1.23)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-47.11, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=432.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(480.0)
            with Note(default_x=30.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-93.66)
                Staff(1)
            with Note(default_x=72.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=252.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=295.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=337.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=390.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=432.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=72.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=114.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=295.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=337.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(96.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=30.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=167.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=252.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=390.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(96.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-103.58)
                Staff(2)
            with Note(default_x=30.2, default_y=-166.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=30.2, default_y=-146.08):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural-sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=30.2, default_y=-131.08):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=141.44, default_y=-201.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=62.66)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.43)
                Staff(2)
            with Note(default_x=252.68, default_y=-151.08):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=252.68, default_y=-141.08):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=252.68, default_y=-121.08):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=363.91, default_y=-201.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=363.91, default_y=-166.08):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=78.64)
                Staff(2)
        with Measure(number='33', width=485.3):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-53.81, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=18.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=207.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('natural-sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-63.81, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-105.06)
                Staff(1)
            with Note(default_x=250.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=440.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=18.16, default_y=-30.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=120.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=164.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural-sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Note(default_x=250.93, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=318.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=353.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=396.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=440.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=85.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=120.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=318.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=353.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=18.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=164.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=250.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=396.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-114.15)
                Staff(2)
            with Note(default_x=17.8, default_y=-161.08):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
            with Backup():
                Duration(480.0)
            with Note(default_x=18.16, default_y=-196.08):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=120.71, default_y=-156.08):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=120.71, default_y=-146.08):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=120.71, default_y=-136.08):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=93.38)
                Staff(2)
            with Note(default_x=353.48, default_y=-156.08):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=353.48, default_y=-146.08):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=353.48, default_y=-136.08):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='34', width=605.75):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(173.31)
                with StaffLayout(number=2):
                    StaffDistance(111.92)
            with Note(default_x=144.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=331.27, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=374.16, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=561.26, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=144.17, default_y=-30.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=245.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=288.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=331.27, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=374.16, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=441.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=475.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=518.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=561.26, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=211.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=245.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=441.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=475.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=144.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=288.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=374.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=518.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-114.15)
                Staff(2)
            with Note(default_x=143.81, default_y=-171.92):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
            with Backup():
                Duration(480.0)
            with Note(default_x=144.17, default_y=-206.92):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=245.5, default_y=-166.92):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=245.5, default_y=-156.92):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=245.5, default_y=-146.92):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=93.38)
                Staff(2)
            with Note(default_x=475.49, default_y=-166.92):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=475.49, default_y=-156.92):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=475.49, default_y=-146.92):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=475.67):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.83, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=62.66)
                Staff(1)
            with Note(default_x=17.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=203.39, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=61.3)
                Staff(1)
            with Note(default_x=245.93, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-2.46)
                Staff(1)
            with Note(default_x=431.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=84.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=118.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=160.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.39, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=245.93, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=312.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=346.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=388.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=431.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=84.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=118.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=312.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=346.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=160.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=245.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=388.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-114.15)
                Staff(2)
            with Note(default_x=17.8, default_y=-171.92):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-206.92):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=118.31, default_y=-156.92):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=118.31, default_y=-146.92):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=245.93, default_y=-161.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=245.93, default_y=-141.92):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=346.44, default_y=-206.92):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='36', width=467.49):
            with Note(default_x=36.11, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Accent()
            with Backup():
                Duration(480.0)
            with Note(default_x=36.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=99.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=131.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=25.3, relative_x=18.4)
                Staff(1)
            with Note(default_x=171.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=19.63)
                Staff(1)
            with Note(default_x=251.18, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=313.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=345.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=385.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=425.85, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(120.0)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=171.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=251.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(360.0)
            with Note(default_x=36.47, default_y=-146.92):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-10.0)
                Staff(2)
            with Note(default_x=131.07, default_y=-141.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=251.18, default_y=-146.92):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=345.77, default_y=-156.92):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note(default_x=23.52, default_y=-171.92):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=36.11, default_y=-166.92):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=36.11, default_y=-156.92):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='37', width=579.75):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(161.52)
                with StaffLayout(number=2):
                    StaffDistance(95.57)
            with Note(default_x=144.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-83.65)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=320.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-56.22, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-93.67)
                Staff(1)
            with Note(default_x=361.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=537.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=144.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=239.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=280.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=320.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=361.16, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=424.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=456.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=497.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=537.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=207.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=239.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=424.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=456.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=280.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=361.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=497.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-114.15)
                Staff(2)
            with Note(default_x=143.81, default_y=-155.57):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
            with Backup():
                Duration(480.0)
            with Note(default_x=144.17, default_y=-190.57):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=239.77, default_y=-150.57):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=239.77, default_y=-140.57):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=239.77, default_y=-130.57):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=93.38)
                Staff(2)
            with Note(default_x=456.76, default_y=-150.57):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=456.76, default_y=-140.57):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=456.76, default_y=-130.57):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='38', width=482.19):
            with Note(default_x=17.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=206.05, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=249.2, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=437.44, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-30.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=119.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=162.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.05, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=249.2, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=316.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=351.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=394.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=437.44, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=85.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=119.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=316.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=351.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=162.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=249.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=394.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-84.1)
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-190.57):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=17.8, default_y=-155.57):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=119.75, default_y=-150.57):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=119.75, default_y=-140.57):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=119.75, default_y=-130.57):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=93.38)
                Staff(2)
            with Note(default_x=351.14, default_y=-140.57):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=351.14, default_y=-130.57):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='39', width=486.97):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.83, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=75.88, relative_x=17.2)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-95.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-95.0)
                Staff(1)
            with Note(default_x=17.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-2.46)
                Staff(1)
            with Note(default_x=207.99, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=77.71, relative_x=17.2)
                Staff(1)
            with Note(default_x=251.58, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=1.23)
                Staff(1)
            with Note(default_x=441.77, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=120.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=164.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.99, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=251.58, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=319.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=354.58, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=398.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=441.77, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=85.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=120.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=319.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=354.58, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=164.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=251.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=398.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.03)
                Staff(2)
            with Note(default_x=17.8, default_y=-195.57):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=17.8, default_y=-160.57):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=120.8, default_y=-140.57):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=120.8, default_y=-130.57):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=120.8, default_y=-115.57):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.03)
                Staff(2)
            with Note(default_x=251.58, default_y=-195.57):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=251.58, default_y=-160.57):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=354.58, default_y=-135.57):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=354.58, default_y=-110.57):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='40', width=611.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(186.52)
                with StaffLayout(number=2):
                    StaffDistance(90.77)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=75.0)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-95.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-95.0)
                Staff(1)
            with Note(default_x=143.81, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-19.66)
                Staff(1)
            with Note(default_x=333.43, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=75.0)
                Staff(1)
            with Note(default_x=376.89, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-15.97)
                Staff(1)
            with Note(default_x=566.51, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=143.81, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=246.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=289.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.43, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=376.89, default_y=-5.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=444.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=479.58, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=523.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=566.51, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=211.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=246.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=444.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=479.58, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=143.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=289.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=376.89, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=523.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.53)
                Staff(2)
            with Note(default_x=143.81, default_y=-190.77):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=143.81, default_y=-155.77):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=246.5, default_y=-135.77):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=246.5, default_y=-120.77):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=246.5, default_y=-110.77):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.53)
                Staff(2)
            with Note(default_x=376.89, default_y=-190.77):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=376.89, default_y=-155.77):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=479.58, default_y=-140.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=479.58, default_y=-130.77):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=479.58, default_y=-115.77):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='41', width=473.52):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=75.0)
                Staff(1)
            with Note(default_x=17.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-19.66)
                Staff(1)
            with Note(default_x=202.52, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-3.69, relative_y=-59.79):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=65.0)
                Staff(1)
            with Note(default_x=244.86, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-15.97)
                Staff(1)
            with Note(default_x=429.58, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=83.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=117.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=160.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.52, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=244.86, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=311.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=344.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=387.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=429.58, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=83.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=117.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=311.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=344.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=160.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=244.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=387.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.53)
                Staff(2)
            with Note(default_x=17.8, default_y=-190.77):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=17.8, default_y=-155.77):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=117.84, default_y=-145.77):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=117.84, default_y=-120.77):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.53)
                Staff(2)
            with Note(default_x=244.86, default_y=-205.77):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=244.86, default_y=-170.77):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=344.9, default_y=-140.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=344.9, default_y=-125.77):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='42', width=463.81):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=55.0)
                Staff(1)
            with Note(default_x=17.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-19.66)
                Staff(1)
            with Note(default_x=198.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=55.0)
                Staff(1)
            with Note(default_x=240.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-15.97)
                Staff(1)
            with Note(default_x=420.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=82.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=115.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=157.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=240.01, default_y=-30.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('decresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-93.8)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-93.8)
                Staff(1)
            with Note(default_x=304.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=337.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=379.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=420.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=82.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=115.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=304.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=337.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=157.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=240.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=379.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-140.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=17.8, default_y=-125.77):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=115.7, default_y=-140.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=115.7, default_y=-125.77):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(240.0)
            with Note(default_x=240.01, default_y=-160.77):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=337.91, default_y=-135.77):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(240.0)
            with Note(default_x=240.01, default_y=-160.77):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='43', width=589.03):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(74.85)
                with StaffLayout(number=2):
                    StaffDistance(74.6)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=55.0)
                Staff(1)
            with Note(default_x=135.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-19.66)
                Staff(1)
            with Note(default_x=319.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=55.0)
                Staff(1)
            with Note(default_x=361.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-15.97)
                Staff(1)
            with Note(default_x=545.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=135.01, default_y=-35.0, print_object='no'):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=200.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=234.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=276.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=361.22, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=427.11, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=460.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=503.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=545.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=200.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=234.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=135.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=276.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=503.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.15)
                Staff(2)
            with Note(default_x=135.01, default_y=-174.6):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=234.67, default_y=-139.6):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=234.67, default_y=-119.6):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.3, relative_y=-25.0):
                        Fz()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=361.22, default_y=-99.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='44', width=459.89):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=55.0)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-108.8)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-108.8)
                Staff(1)
            with Note(default_x=14.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-19.66)
                Staff(1)
            with Note(default_x=194.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=55.0)
                Staff(1)
            with Note(default_x=236.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-15.97)
                Staff(1)
            with Note(default_x=416.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=14.0, default_y=-45.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=78.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=111.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=153.3, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=236.14, default_y=-45.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=300.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=334.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=375.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=416.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=14.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=153.3, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=236.14, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=375.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.15)
                Staff(2)
            with Note(default_x=236.14, default_y=-159.6):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=5.51)
            with Note(default_x=236.14, default_y=-139.6):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=5.51)
            with Note(default_x=236.14, default_y=-114.6):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=5.51)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='45', width=499.99):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=53.77, relative_x=12.29)
                Staff(1)
            with Note(default_x=16.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-19.66)
                Staff(1)
            with Note(default_x=195.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note():
                Rest()
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Staff(1)
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Note(default_x=341.96, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=374.91, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=416.07, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=457.23, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note(default_x=16.09, default_y=-45.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=80.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=113.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=154.49, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(120.0)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=416.07, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(240.0)
            with Note(default_x=16.09, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Tuplet(type='stop')
            with Forward():
                Duration(80.0)
            with Backup():
                Duration(240.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.15)
                Staff(2)
            with Note(default_x=16.09, default_y=-174.6):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=16.09, default_y=-154.6):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=16.09, default_y=-129.6):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=236.81, default_y=-134.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=236.81, default_y=-99.6):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='46', width=608.7):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=143.81, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=332.26, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=375.46, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=563.91, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note(default_x=143.81, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.29, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=245.87, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=289.07, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=332.26, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=375.46, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=442.93, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=477.52, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=520.71, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=563.91, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=143.81, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=289.07, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=375.46, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=520.71, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-135.9)
                Staff(2)
            with Note(default_x=375.46, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=375.46, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='47', width=468.86):
            with Direction(placement='below'):
                with DirectionType():
                    Words('molto rall.', default_y=-47.2, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=66.67, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('74')
                Staff(1)
                Sound(tempo=74.0)
            with Note(default_x=17.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Accent()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=65.35, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Staff(1)
                Sound(tempo=68.0)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-83.8)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-83.8)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=200.62, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=66.67, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('62')
                Staff(1)
                Sound(tempo=62.0)
            with Note(default_x=242.53, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Accent()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=65.35, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('56')
                Staff(1)
                Sound(tempo=56.0)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(default_x=425.35, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=83.26, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=116.81, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=158.72, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.62, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=242.53, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=307.99, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=341.54, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=383.44, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=425.35, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=158.72, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=242.53, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=383.44, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-135.9)
                Staff(2)
            with Note(default_x=17.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=17.8, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='48', width=471.35):
            with Direction(placement='below'):
                with DirectionType():
                    Words('smorz.', default_y=-40.0, relative_y=-45.0, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=65.02, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('50')
                Staff(1)
                Sound(tempo=50.0)
            with Note(default_x=17.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=66.04, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('44')
                Staff(1)
                Sound(tempo=44.0)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.8, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=221.04, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=13.03, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('20')
                Staff(1)
                Sound(tempo=20.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Tempo I', default_y=10.6, relative_y=20.0, font_weight='bold', font_size='13')
                Staff(1)
                Sound(tempo=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        OtherDynamics('dolce')
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=359.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=432.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(480.0)
            with Note(default_x=17.8, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(90.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=90.57, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=127.87, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=174.45, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.04, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(240.0)
            with Note(print_object='no'):
                Rest()
                Duration(90.0)
                Voice('3')
                Type('16th')
                Dot()
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(30.0)
                Voice('3')
                Type('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('3')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(240.0)
            with Note(default_x=17.8, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('4')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('4')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=174.45, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
                Voice('4')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(240.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='49', width=374.94):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(159.83)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=37.98, relative_x=14.74)
                Staff(1)
            with Note(default_x=135.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.07, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-33.17)
                Staff(1)
            with Note(default_x=274.27, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=323.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.01)
                Staff(2)
            with Note(default_x=135.01, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=207.07, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.27, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.27, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=323.81, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='50', width=413.94):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-78.17)
                Staff(1)
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=69.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=99.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=130.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.17, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=160.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=191.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=246.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=267.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=287.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=318.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=338.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=359.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=389.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(17.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.01)
                Staff(2)
            with Note(default_x=13.8, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.03, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.45, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.45, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=246.68, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='51', width=760.02):
            with Direction(placement='above'):
                with DirectionType():
                    Words('leggieriss.', default_y=84.0, relative_y=-35.0, font_style='italic', font_size='9')
                Staff(1)
            with Note(default_x=9.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=31.72, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=48.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=64.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=87.5, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=103.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=124.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=152.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural-sharp')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=185.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=202.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=218.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=238.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=258.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=275.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=291.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=308.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=324.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=347.29, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=367.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=383.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=403.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=420.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=442.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=462.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=485.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=505.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=521.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=538.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=554.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=571.24, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=593.58, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=610.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=626.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=648.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=671.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=687.74, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=704.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=720.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=737.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(40)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.01)
                Staff(2)
            with Note(default_x=7.41, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=200.34, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=381.88, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=381.88, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=569.27, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(120.0)
            with Note(default_x=200.34, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(120.0)
        with Measure(number='52', width=465.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(82.76)
            with Note(default_x=131.21, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=149.65, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=199.34, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=225.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=252.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=279.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
            with Note(default_x=322.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('backward hook', number=4)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=338.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=388.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=434.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.52)
                Staff(2)
            with Note(default_x=149.65, default_y=-167.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=199.34, default_y=-147.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=338.77, default_y=-132.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=338.77, default_y=-122.76):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=338.77, default_y=-112.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='53', width=264.58):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=135.45, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=159.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=211.02, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.52)
                Staff(2)
            with Note(default_x=13.8, default_y=-177.76):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=89.37, default_y=-142.76):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=159.07, default_y=-132.76):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=159.07, default_y=-112.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=211.02, default_y=-142.76):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='54', width=500.16):
            with Note(default_x=13.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=53.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('natural-sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('con forza', default_y=76.0, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=134.05, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-65.81, relative_x=-1.23)
                Staff(1)
            with Note(default_x=197.95, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=223.0, default_y=45.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=248.05, default_y=40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=273.1, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=298.16, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=323.21, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=348.26, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=373.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=398.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=423.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=448.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-3.69)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-52.56, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=473.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.52)
                Staff(2)
            with Note(default_x=13.8, default_y=-197.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-162.76):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=134.05, default_y=-142.76):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=122.18, default_y=-132.76):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural-sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=134.05, default_y=-127.76):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=134.05, default_y=-117.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.52)
                Staff(2)
            with Note(default_x=197.95, default_y=-187.76):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=197.95, default_y=-152.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=336.39, default_y=-132.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=348.26, default_y=-127.76):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=348.26, default_y=-117.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=348.26, default_y=-107.76):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='55', width=318.78):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=78.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=136.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=165.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=207.6, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=218.56, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=230.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=287.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-107.76):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=78.59, default_y=-107.76):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=165.49, default_y=-117.76):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=230.28, default_y=-112.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=287.73, default_y=-117.76):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.44, default_y=-147.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(120.0)
            with Note(default_x=78.59, default_y=-132.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('8')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=230.28, default_y=-137.76):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(90.0)
                Voice('8')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=287.73, default_y=-117.76):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(30.0)
                Voice('8')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='56', width=687.45):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(162.98)
                with StaffLayout(number=2):
                    StaffDistance(111.08)
            with Note(default_x=143.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(90.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=227.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=271.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=325.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=379.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=411.36, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=422.33, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=434.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=506.87, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=517.84, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=529.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Staff(1)
            with Note(default_x=642.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(480.0)
            with Note(default_x=143.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=529.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note(default_x=143.25, default_y=-151.08):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=271.37, default_y=-136.08):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=434.04, default_y=-146.08):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=529.55, default_y=-141.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(90.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=642.43, default_y=-146.08):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(480.0)
            with Note(default_x=143.25, default_y=-176.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(360.0)
            with Forward():
                Duration(360.0)
            with Note(default_x=529.55, default_y=-176.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(90.0)
                Tie(type='stop')
                Voice('8')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=642.43, default_y=-176.08):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(30.0)
                Voice('8')
                Type('32nd')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='57', width=861.46):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=76.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=196.28, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
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
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=239.47, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=282.66, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
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
                    with Articulations():
                        Staccato()
            with Note(default_x=325.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=369.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.  e rall.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-96.71)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-96.71)
                Staff(1)
            with Note(default_x=412.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    with Articulations():
                        Staccato()
            with Note(default_x=449.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=486.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=524.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=561.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=598.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=636.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    with Articulations():
                        Staccato()
            with Note(default_x=673.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=710.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='stop')
                    with Articulations():
                        Accent()
            with Note(default_x=747.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=785.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=822.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=412.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(180.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=747.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(480.0)
            with Note(default_x=17.23, default_y=-171.08):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=17.23, default_y=-151.08):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=196.28, default_y=-181.08):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=196.28, default_y=-151.08):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=412.23, default_y=-176.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=412.23, default_y=-156.08):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(120.0)
            with Note(default_x=196.28, default_y=-136.08):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=636.05, default_y=-136.08):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('6')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=747.95, default_y=-136.08):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Tie(type='stop')
                Voice('6')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=785.26, default_y=-141.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=822.56, default_y=-146.08):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='58', width=789.16):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(114.37)
                with StaffLayout(number=2):
                    StaffDistance(98.1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=135.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=60.5)
                Staff(1)
            with Note(default_x=231.5, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=413.04, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=486.83, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=524.66, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=562.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=600.3, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=674.09, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=711.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=749.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=135.01, default_y=-218.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=231.5, default_y=-163.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=231.5, default_y=-138.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
            with Note(default_x=292.01, default_y=-163.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.01, default_y=-138.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
            with Note(default_x=352.53, default_y=-163.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=352.53, default_y=-138.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
            with Note(default_x=413.04, default_y=-148.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=413.04, default_y=-138.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=413.04, default_y=-128.1):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=600.3, default_y=-163.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=600.3, default_y=-148.1):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=600.3, default_y=-138.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='59', width=759.75):
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=13.8, default_y=40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=87.13, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=124.71, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=162.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=199.89, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=273.22, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=310.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=348.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=385.97, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=459.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=496.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=534.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=572.06, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=645.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=682.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=720.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-183.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=199.89, default_y=-163.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=199.89, default_y=-148.1):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=199.89, default_y=-138.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=273.22, default_y=-163.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=273.22, default_y=-148.1):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
            with Note(default_x=273.22, default_y=-138.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
            with Note(default_x=310.8, default_y=-163.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=310.8, default_y=-148.1):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
            with Note(default_x=310.8, default_y=-138.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
            with Note(default_x=348.39, default_y=-163.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=348.39, default_y=-148.1):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
            with Note(default_x=348.39, default_y=-138.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
            with Note(default_x=385.97, default_y=-148.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=385.97, default_y=-138.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=385.97, default_y=-128.1):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=572.06, default_y=-163.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=572.06, default_y=-148.1):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=572.06, default_y=-138.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='60', width=798.02):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(119.28)
                with StaffLayout(number=2):
                    StaffDistance(85.89)
            with Note(default_x=144.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=171.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=198.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=225.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=252.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=280.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=307.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=334.5, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=361.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=388.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=416.01, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=-67.21, relative_x=9.83)
                Staff(1)
            with Note(default_x=443.19, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=470.36, default_y=-110.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Direction(placement='below'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none', relative_x=-8.6)
                Staff(1)
            with Note(default_x=497.53, default_y=-115.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=524.7, default_y=-125.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=551.87, default_y=-135.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=579.04, default_y=-150.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=606.21, default_y=-125.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=633.39, default_y=-110.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=660.56, default_y=-115.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=687.73, default_y=-125.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=714.9, default_y=-135.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=742.07, default_y=-150.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=769.24, default_y=-125.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=144.3, default_y=-170.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=144.3, default_y=-150.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=144.3, default_y=-125.89):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-126.65)
                Staff(2)
            with Note(default_x=633.39, default_y=-185.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='61', width=650.7):
            with Direction(placement='below'):
                with DirectionType():
                    Words('smorz.', default_y=-40.0, relative_x=-4.91, relative_y=-25.17, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('36')
                Staff(1)
                Sound(tempo=36.0)
            with Note(default_x=13.8, default_y=-110.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=40.27, default_y=-115.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=66.74, default_y=-125.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=93.21, default_y=-135.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=119.68, default_y=-150.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=146.15, default_y=-125.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('32')
                Staff(1)
                Sound(tempo=32.0)
            with Note(default_x=172.62, default_y=-110.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=199.1, default_y=-115.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=225.57, default_y=-125.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=252.04, default_y=-135.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=278.51, default_y=-150.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=304.98, default_y=-125.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('28')
                Staff(1)
                Sound(tempo=28.0)
            with Note(default_x=331.45, default_y=-110.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=357.92, default_y=-115.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=384.39, default_y=-125.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=410.86, default_y=-135.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=437.33, default_y=-150.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=463.8, default_y=-125.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('24')
                Staff(1)
                Sound(tempo=24.0)
            with Note(default_x=490.27, default_y=-110.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=516.74, default_y=-115.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=543.21, default_y=-125.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=569.69, default_y=-135.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=596.16, default_y=-150.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=-110.0, relative_x=20.0)
                Staff(1)
            with Note(default_x=622.63, default_y=-115.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none', relative_x=53.17)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-126.65)
                Staff(2)
            with Note(default_x=13.8, default_y=-205.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-170.89):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=490.27, default_y=-185.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='62', width=100.19):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=46.67)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=15.18, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('20')
                Staff(1)
                Sound(tempo=20.0)
            with Note(default_x=34.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
            with Backup():
                Duration(480.0)
            with Note(default_x=34.64, default_y=-205.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(480.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')