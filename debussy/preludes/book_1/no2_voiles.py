with ScorePartwise(version='3.1'):
    with Identification():
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
            PageHeight(1683.25)
            PageWidth(1190.8)
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
        CreditWords('Debussy - Préludes - Book I - II', default_x=595.402, default_y=1626.56, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Voiles', default_x=595.402, default_y=1569.88, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Claude Debussy', default_x=1134.12, default_y=1526.56, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Piano')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=302.27):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(86.1)
                        RightMargin(0.0)
                    TopSystemDistance(221.4)
                with StaffLayout(number=2):
                    StaffDistance(310.14)
            with Attributes():
                Divisions(480.0)
                with Key():
                    Fifths(0)
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
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Modéré ( \n', default_y=81.21, font_family='Times New Roman')
                with DirectionType():
                    with Metronome(parentheses='no', default_y=81.21):
                        BeatUnit('eighth')
                        PerMinute('88')
                with DirectionType():
                    Words(' )\n', default_y=81.21, font_family='Times New Roman')
                    Words('(Dans un rythme sans rigueur et caressant.)')
                Staff(1)
            with Note(default_x=143.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=143.54, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('très doux', default_y=107.0, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=193.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
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
                    Slur(type='stop', number=1)
            with Note(default_x=193.18, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=224.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=224.58, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=247.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=247.14, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=277.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=277.51, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=7.5, default_y=-40.0, relative_x=134.47, relative_y=-46.98):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note():
                Rest(measure='yes')
                Duration(960.0)
                Voice('5')
                Staff(2)
        with Measure(number='2', width=221.21):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-326.79)
                Staff(1)
            with Note(default_x=16.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=16.2, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=81.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=81.01, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=2, default_y=-327.17)
                Staff(1)
            with Note(default_x=152.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=152.01, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-100.0)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-30.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest(measure='yes')
                Duration(960.0)
                Voice('5')
                Staff(2)
        with Measure(number='3', width=234.84):
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-286.0, relative_x=82.7, relative_y=-44.74):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=76.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=76.11, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-325.74)
                Staff(1)
            with Note(default_x=125.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
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
                    Slur(type='stop', number=1)
            with Note(default_x=125.75, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=157.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=157.15, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=179.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=179.71, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=210.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=210.08, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-30.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest(measure='yes')
                Duration(960.0)
                Voice('5')
                Staff(2)
        with Measure(number='4', width=233.0):
            with Direction(placement='above'):
                with DirectionType():
                    Words('più', default_y=60.96, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=16.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=16.2, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-284.38, relative_x=40.3, relative_y=-43.9):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-323.28)
                Staff(1)
            with Note(default_x=79.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=79.5, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=145.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.09, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=173.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.86, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=202.63, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=202.63, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-20.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest(measure='yes')
                Duration(960.0)
                Voice('5')
                Staff(2)
        with Measure(number='5', width=199.26):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(89.21)
            with Note(default_x=61.11, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=61.11, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=92.37, relative_y=-171.63):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=129.56, default_y=-194.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='6', width=199.23):
            with Note(default_x=20.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=20.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-194.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=63.68, default_y=-194.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=151.05, default_y=-194.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='7', width=226.83):
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=33.47, relative_y=-45.21):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('expressif', default_y=41.01, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=71.31, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=122.62, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=173.92, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=173.92, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('toujours', default_y=11.8, font_style='italic', font_family='Times New Roman')
                Staff(2)
            with Note(default_x=71.31, default_y=-164.21):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=122.62, default_y=-159.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_x=153.33, relative_y=-173.46):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-194.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='8', width=202.78):
            with Note(default_x=20.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(480.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=20.0, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=110.59, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=110.59, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-194.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=65.29, default_y=-194.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=155.88, default_y=-194.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='9', width=226.83):
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=71.31, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=122.62, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=173.92, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=173.92, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=71.31, default_y=-164.21):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=122.62, default_y=-159.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-194.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='10', width=319.66):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(968.53)
            with Note(default_x=59.31, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=59.31, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('très doux', default_y=52.86, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=169.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=169.22, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=213.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=213.16, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=244.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=244.56, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=264.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=264.53, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=294.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=294.9, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-1015.39)
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=169.22, default_y=-1028.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Tenuto()
            with Note(default_x=169.22, default_y=-993.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-190.0)
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=59.31, default_y=-1073.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=103.25, default_y=-1073.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=213.16, default_y=-1073.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='11', width=180.49):
            with Note(default_x=20.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=20.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-1028.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=20.0, default_y=-993.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.72, default_y=-1023.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.72, default_y=-988.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-1108.51)
                Staff(2)
            with Note(default_x=99.44, default_y=-1028.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=99.44, default_y=-993.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=139.17, default_y=-1033.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=139.17, default_y=-998.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=210.0)
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-1073.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='12', width=294.67):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=17.23, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=85.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
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
                    Slur(type='stop', number=1)
            with Note(default_x=85.59, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=116.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=116.99, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=138.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=138.35, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=168.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=168.71, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=199.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=199.08, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note(default_x=17.23, default_y=-1038.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=17.23, default_y=-1003.53):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=51.41, default_y=-1043.53):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=51.41, default_y=-1008.53):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=85.59, default_y=-1038.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=85.59, default_y=-1003.53):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=246.08, default_y=-1043.53):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=246.08, default_y=-1008.53):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='13', width=260.11):
            with Note(default_x=16.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=16.2, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-995.83)
                Staff(1)
            with Note(default_x=82.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=82.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=113.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=113.16, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=141.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.11, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=169.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Tenuto()
            with Note(default_x=169.06, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-13.85)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=15.84, default_y=-1043.53):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(960.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=15.84, default_y=-1008.53):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=113.16, default_y=-1073.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=213.79, default_y=-1073.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='14', width=179.85):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(1340.64)
            with Note(default_x=69.94, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    with Articulations():
                        Tenuto()
            with Note(default_x=69.94, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=69.58, default_y=-1415.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(960.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=69.58, default_y=-1380.64):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=104.83, default_y=-1445.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=153.77, default_y=-1445.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='15', width=365.51):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=11.87, relative_y=-44.8):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=20.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=20.0, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=103.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
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
                    Slur(type='stop', number=1)
            with Note(default_x=103.17, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=134.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=134.56, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=156.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=156.0, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=186.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=186.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=216.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=216.73, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(1200.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=103.17, default_y=-1440.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=103.17, default_y=-1430.64):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=103.17, default_y=-1420.64):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=103.17, default_y=-1405.64):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=216.73, default_y=-1435.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=216.73, default_y=-1425.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=216.73, default_y=-1415.64):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=216.73, default_y=-1400.64):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=283.89, default_y=-1480.64):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=283.89, default_y=-1460.64):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=283.89, default_y=-1430.64):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=283.89, default_y=-1410.64):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=314.21, default_y=-1430.64, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=314.21, default_y=-1420.64, print_object='no', dynamics=0.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=314.21, default_y=-1405.64, print_object='no', dynamics=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=314.21, default_y=-1395.64, print_object='no', dynamics=0.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(1200.0)
            with Note(default_x=20.0, default_y=-1445.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Forward():
                Duration(240.0)
        with Measure(number='16', width=172.69):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-1349.33)
                Staff(1)
            with Note(default_x=20.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(420.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=20.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(420.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=70.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=70.14, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=2, default_y=-1349.33)
                Staff(1)
            with Note(default_x=117.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=117.94, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-111.56)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-30.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-1445.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=46.57, default_y=-1445.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=144.51, default_y=-1445.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='17', width=336.89):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-1307.8, relative_x=13.39, relative_y=-46.53):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=20.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=20.0, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=87.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
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
                    Slur(type='stop', number=1)
            with Note(default_x=87.98, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=119.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=119.38, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=138.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=138.91, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=169.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=169.28, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=199.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=199.64, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=285.6, default_y=-25.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=285.6, default_y=-15.0, print_object='no', dynamics=0.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(1200.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=87.98, default_y=-1440.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=87.98, default_y=-1430.64):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=87.98, default_y=-1420.64):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=87.98, default_y=-1405.64):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=199.64, default_y=-1435.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=199.64, default_y=-1425.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=199.64, default_y=-1415.64):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=199.64, default_y=-1400.64):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=242.62, default_y=-1430.64):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=242.62, default_y=-1420.64):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=242.62, default_y=-1405.64):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=242.62, default_y=-1395.64):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=285.6, default_y=-1430.64, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=285.6, default_y=-1420.64, print_object='no', dynamics=0.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=285.6, default_y=-1405.64, print_object='no', dynamics=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=285.6, default_y=-1395.64, print_object='no', dynamics=0.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(1200.0)
            with Note(default_x=20.0, default_y=-1445.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Forward():
                Duration(240.0)
        with Measure(number='18', width=275.09):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(155.5)
                with StaffLayout(number=2):
                    StaffDistance(168.41)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=58.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(420.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=58.37, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(420.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=144.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=144.03, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=168.65, relative_y=-46.95):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=164.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=164.67, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=250.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=250.33, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-176.09)
                Staff(2)
            with Note(default_x=58.37, default_y=-273.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=103.77, default_y=-273.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-176.09)
                Staff(2)
            with Note(default_x=210.07, default_y=-273.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-150.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2)
                Staff(2)
        with Measure(number='19', width=356.22):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=8.9, relative_y=-44.66):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=20.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=20.0, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=153.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=153.74, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=179.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=179.93, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1200.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-210.9)
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(1)
            with Note(default_x=102.63, default_y=-278.41):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=102.63, default_y=-268.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=102.63, default_y=-258.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=102.63, default_y=-243.41):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=179.93, default_y=-273.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=179.93, default_y=-263.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=179.93, default_y=-248.41):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=179.93, default_y=-238.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=237.56, default_y=-268.41):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=237.56, default_y=-258.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=237.56, default_y=-243.41):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=237.56, default_y=-233.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=295.19, default_y=-268.41, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=295.19, default_y=-258.41, print_object='no'):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=295.19, default_y=-243.41, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=295.19, default_y=-233.41, print_object='no'):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-190.0)
                Staff(2)
            with Backup():
                Duration(1200.0)
            with Note(default_x=20.0, default_y=-273.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(240.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(240.0)
            with Forward():
                Duration(240.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Forward():
                Duration(240.0)
        with Measure(number='20', width=234.52):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=20.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=20.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=70.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=70.1, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-124.51)
                Staff(1)
            with Note(default_x=120.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=120.2, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=201.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=201.61, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-273.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=70.1, default_y=-273.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=170.3, default_y=-273.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=189.1):
            with Note(default_x=20.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=20.36, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-124.51, relative_x=56.51, relative_y=-64.5):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=94.84, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('3')
                Type('quarter')
                Staff(1)
            with Note(default_x=94.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=94.84, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(240.0)
                Voice('3')
                Type('eighth')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.36, default_y=-273.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=296.12):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(342.02)
                with StaffLayout(number=2):
                    StaffDistance(436.44)
            with Note(default_x=61.11, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=61.11, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('très souple', default_y=62.79, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=190.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=220.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=239.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=271.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(960.0)
            with Note(default_x=61.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=147.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Tenuto()
            with Backup():
                Duration(960.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=181.39, relative_y=-47.73):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=60.75, default_y=-541.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='23', width=350.33):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-428.91)
                Staff(1)
            with Note(default_x=18.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=53.2, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=118.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=118.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=189.19, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=189.19, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-112.25, relative_x=229.88, relative_y=-30.54):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=259.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=281.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=303.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=325.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-250.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=18.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=153.99, default_y=-50.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=189.19, default_y=-486.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=303.57, default_y=-466.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(960.0)
            with Note(default_x=30.34, default_y=-541.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=18.01, default_y=-466.44, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('7')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=153.99, default_y=-466.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('7')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('7')
                Type('quarter')
                Staff(2)
        with Measure(number='24', width=408.48):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-431.17)
                Staff(1)
            with Note(default_x=20.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=55.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=55.89, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=120.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=120.49, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=190.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=190.83, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-421.73)
                Staff(1)
            with Note(default_x=261.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=283.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=305.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=336.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=358.52, default_y=15.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-300.0)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-60.0)
                Staff(1)
            with Backup():
                Duration(1200.0)
            with Note(default_x=20.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=155.66, default_y=-50.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=190.83, default_y=-486.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=305.14, default_y=-466.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(1200.0)
            with Note(default_x=20.36, default_y=-541.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note(default_x=20.36, default_y=-466.44, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('7')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=155.66, default_y=-466.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('7')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('7')
                Type('quarter')
                Staff(2)
            with Forward():
                Duration(240.0)
        with Measure(number='25', width=342.78):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(751.48)
            with Note(default_x=58.37, default_y=5.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=102.87, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=122.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=122.77, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=153.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=153.14, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=222.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=222.12, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-737.56)
                Staff(1)
            with Note(default_x=259.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=259.7, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=283.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=283.28, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=317.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
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
            with Note(default_x=317.61, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-75.81)
                Staff(1)
            with Backup():
                Duration(1200.0)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=102.51, default_y=-776.48):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=190.72, default_y=-781.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=222.12, default_y=-801.48):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=300.44, default_y=-781.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1200.0)
            with Note(default_x=58.37, default_y=-856.48, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=102.51, default_y=-856.48):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=247.21):
            with Note(default_x=15.7, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=48.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Cédez   -         -               -              -//', default_y=17.8, font_weight='bold', font_family='Times New Roman')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-740.15)
                Staff(1)
            with Note(default_x=165.39, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
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
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=165.39, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=188.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=188.11, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=222.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(80.0)
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
                    with Articulations():
                        Tenuto()
            with Note(default_x=222.44, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-60.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=28.9, default_y=-35.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('3')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=48.84, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(720.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('3')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=60.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('4')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.77, default_y=-50.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('4')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('4')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=60.48, default_y=-771.48, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=97.77, default_y=-781.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=129.17, default_y=-801.48):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=205.27, default_y=-781.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(960.0)
            with Note(default_x=48.48, default_y=-856.48):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='27', width=197.12):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-701.3, relative_x=5.98, relative_y=-43.86):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-740.15)
                Staff(1)
            with Note(default_x=16.46, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=49.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-50.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=61.19, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(720.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=29.66, default_y=-35.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('3')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=49.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('3')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(960.0)
            with Note(default_x=60.6, default_y=-771.48, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=88.98, default_y=-781.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.37, default_y=-801.48):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=172.36, default_y=-781.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(960.0)
            with Note(default_x=49.6, default_y=-856.48):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='28', width=267.82):
            with Direction(placement='above'):
                with DirectionType():
                    Words('a Tempo', default_y=41.2, font_weight='bold', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=16.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=128.19, relative_y=-28.49):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=130.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=160.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=177.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=210.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=228.12, default_y=-40.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1200.0)
            with Note(default_x=16.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('3')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=91.73, default_y=-50.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('3')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=177.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(960.0)
            with Note(default_x=15.8, default_y=-776.48):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=60.33, default_y=-781.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=91.73, default_y=-801.48):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=177.8, default_y=-766.48, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(1200.0)
            with Note(default_x=15.8, default_y=-856.48):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Forward():
                Duration(240.0)
        with Measure(number='29', width=570.11):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(120.88)
                with StaffLayout(number=2):
                    StaffDistance(1038.92)
            with Note(default_x=58.37, default_y=-25.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=124.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=172.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
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
            with Note(default_x=220.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-1023.71)
                Staff(1)
            with Note(default_x=251.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=281.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=311.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=345.37, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=308.28, relative_y=-27.46):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=441.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=471.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=501.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=534.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-130.0)
                Staff(1)
            with Backup():
                Duration(1200.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=124.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.91, default_y=-1113.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=281.1, default_y=-1108.92):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1200.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('4')
                Type('quarter')
                Staff(1)
            with Note(default_x=220.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('4')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('4')
                Type('eighth')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('4')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(1200.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(1200.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(840.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(840.0)
            with Backup():
                Duration(1200.0)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=345.37, default_y=-1098.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('7')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=393.53, default_y=-1093.92):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('7')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=441.68, default_y=-1088.92):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('7')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=501.88, default_y=-1083.92):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('7')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(1200.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('8')
                Type('eighth')
                Staff(2)
            with Note(default_x=124.23, default_y=-1143.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('8')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='30', width=484.81):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=146.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-1024.73)
                Staff(1)
            with Note(default_x=175.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=204.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=233.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=267.58, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=360.31, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
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
            with Note(default_x=396.28, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=425.26, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=454.24, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-20.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=20.72, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=67.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=67.08, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=146.49, default_y=-1113.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=204.44, default_y=-1108.92):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('4')
                Type('eighth')
                Staff(1)
            with Note(default_x=146.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('4')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('4')
                Type('quarter')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(960.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(720.0)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=267.58, default_y=-1098.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=313.95, default_y=-1093.92):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=360.31, default_y=-1088.92):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=425.26, default_y=-1083.92):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(default_x=20.36, default_y=-1143.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('8')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='31', width=1054.93):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(100.62)
                with StaffLayout(number=2):
                    StaffDistance(1026.98)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-1035.41)
                Staff(1)
            with Note(default_x=68.84, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=306.17, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(30.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=350.12, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(30.0)
                Voice('1')
                Type('64th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=394.07, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(180.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-1001.46, relative_x=162.85, relative_y=-42.83):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=561.08, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=798.42, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(30.0)
                Voice('1')
                Type('64th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=842.37, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(30.0)
                Voice('1')
                Type('64th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=886.32, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(180.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-280.0)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-110.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=68.84, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=139.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=209.48, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(180.0)
                Voice('2')
                Type('16th')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=561.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-1039.29)
                Staff(1)
            with Note(default_x=631.4, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=701.73, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(180.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=68.84, default_y=-1076.98):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=209.48, default_y=-1071.98):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=464.39, default_y=-1071.98):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=561.08, default_y=-1076.98):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=701.73, default_y=-1071.98):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=956.64, default_y=-1071.98):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='32', width=329.25):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(172.43)
                with StaffLayout(number=2):
                    StaffDistance(166.95)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Cédez   -           -              -                -//', default_y=158.43, font_weight='bold', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=71.81, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=71.81, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(960.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=72.17, default_y=-216.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=103.52, default_y=-211.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=134.88, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=166.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    Words('dim.', default_y=5.82, font_style='italic', font_family='Times New Roman')
                Staff(2)
            with Note(default_x=197.6, default_y=-216.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=228.95, default_y=-211.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=260.31, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=291.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='33', width=386.72):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-44.7, relative_x=6.62, relative_y=-40.69):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=20.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=61.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=127.58, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=168.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=213.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=250.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=291.29, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=344.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=127.58, default_y=-20.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=127.58, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=204.44, default_y=-40.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=204.44, default_y=30.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=315.16, default_y=-30.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=315.16, default_y=40.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=127.58, default_y=-266.95):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=127.58, default_y=-256.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=127.58, default_y=-246.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=127.58, default_y=-231.95):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=209.44, default_y=-261.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=209.44, default_y=-251.95):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=209.44, default_y=-241.95):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=209.44, default_y=-226.95):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=291.29, default_y=-256.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=291.29, default_y=-246.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=291.29, default_y=-231.95):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=291.29, default_y=-221.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note(default_x=20.36, default_y=-271.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
        with Measure(number='34', width=338.96):
            with Note(default_x=41.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=74.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=112.26, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=149.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=191.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=224.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=262.33, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=299.85, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(default_x=34.23, default_y=40.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(480.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=184.29, default_y=50.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(480.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Tenuto()
            with Backup():
                Duration(960.0)
            with Note(default_x=37.23, default_y=-256.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.23, default_y=-246.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.23, default_y=-231.95):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.23, default_y=-221.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=187.29, default_y=-251.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Tenuto()
            with Note(default_x=187.29, default_y=-241.95):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=187.29, default_y=-226.95):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=187.29, default_y=-216.95):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note(default_x=36.87, default_y=-271.95, dynamics=0.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=510.75):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(242.36)
                with StaffLayout(number=2):
                    StaffDistance(155.91)
            with Note(default_x=98.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=145.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=206.57, default_y=50.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=249.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=307.24, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=354.71, default_y=-10.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=404.48, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=457.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(default_x=90.86, default_y=-50.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=90.86, default_y=50.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=209.4, default_y=-50.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=210.4, default_y=60.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=300.94, default_y=-25.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=299.94, default_y=50.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=428.35, default_y=-50.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=428.35, default_y=40.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=93.86, default_y=-240.91):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=93.86, default_y=-230.91):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=93.86, default_y=-215.91):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=93.86, default_y=-205.91):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=197.4, default_y=-235.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=197.4, default_y=-220.91):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=197.4, default_y=-210.91):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=197.4, default_y=-200.91):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=300.94, default_y=-240.91):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=300.94, default_y=-230.91):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=300.94, default_y=-215.91):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=300.94, default_y=-205.91):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=404.48, default_y=-245.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=404.48, default_y=-235.91):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=404.48, default_y=-220.91):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=404.48, default_y=-210.91):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=93.5, default_y=-260.91):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
        with Measure(number='36', width=309.87):
            with Note(default_x=73.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=116.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-110.64)
                Staff(1)
            with Note(default_x=139.83, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=167.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=195.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=224.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=252.12, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=280.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-80.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=63.99, default_y=30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.76, default_y=20.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=139.83, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Articulations():
                        Tenuto()
            with Note(default_x=252.12, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Backup():
                Duration(960.0)
            with Note(default_x=68.99, default_y=-250.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=68.99, default_y=-240.91):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=68.99, default_y=-230.91):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=68.99, default_y=-215.91):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=111.76, default_y=-255.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=111.76, default_y=-245.91):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=111.76, default_y=-235.91):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=111.76, default_y=-220.91):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=139.83, default_y=-250.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    Slur(type='start', placement='below', number=3)
            with Note(default_x=139.83, default_y=-240.91):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=139.83, default_y=-230.91):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=139.83, default_y=-215.91):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=252.12, default_y=-255.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=3)
            with Note(default_x=252.12, default_y=-245.91):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=252.12, default_y=-235.91):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=252.12, default_y=-220.91):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=68.63, default_y=-260.91):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='37', width=234.31):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-81.29, relative_x=11.43, relative_y=-34.35):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=25.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=47.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=72.77, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=98.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=130.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=156.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=181.59, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=207.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(default_x=16.36, default_y=20.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.36, default_y=-255.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=20.36, default_y=-245.91):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(960.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=20.36, default_y=-235.91):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=20.36, default_y=-220.91):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Forward():
                Duration(480.0)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=130.47, default_y=-260.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='38', width=381.62):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(433.53)
            with Note(default_x=96.55, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=96.55, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=96.55, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=132.52, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=132.52, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=132.52, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=165.52, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=165.52, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=165.52, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-393.69)
                Staff(1)
            with Note(default_x=247.69, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=247.69, default_y=-35.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=247.69, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=281.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=347.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-70.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=224.52, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_x=70.96, relative_y=-57.95):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=198.52, default_y=-493.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=231.52, default_y=-458.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=314.02, default_y=-463.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=347.02, default_y=-468.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(960.0)
            with Note(default_x=96.19, default_y=-538.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='39', width=321.3):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-342.49, relative_x=21.0, relative_y=-56.2):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=36.23, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=36.23, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=36.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=72.2, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.2, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=72.2, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=105.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=105.2, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=105.2, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=187.37, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=187.37, default_y=-35.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=187.37, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-401.13)
                Staff(1)
            with Note(default_x=220.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-20.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=164.21, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=138.2, default_y=-493.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=171.21, default_y=-458.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=253.7, default_y=-463.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=286.7, default_y=-468.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(960.0)
            with Note(default_x=35.87, default_y=-538.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='40', width=352.0):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Serrez -             -               -               -  /', default_y=53.01, font_weight='bold', font_family='Times New Roman')
                    Words('/', font_weight='normal')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-403.23)
                Staff(1)
            with Note(default_x=28.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=96.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-404.01)
                Staff(1)
            with Note(default_x=190.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=224.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=259.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=304.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-220.0)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-40.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=28.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=178.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=190.44, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('3')
                Type('quarter')
                Staff(1)
            with Note(default_x=190.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('3')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Backup():
                Duration(960.0)
            with Note(default_x=27.87, default_y=-458.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.52, default_y=-463.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=96.81, default_y=-468.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=127.17, default_y=-473.53):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.32, default_y=-483.53):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=190.44, default_y=-458.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=224.73, default_y=-463.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=259.01, default_y=-468.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=287.13, default_y=-473.53):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=322.28, default_y=-483.53):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
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
            with Backup():
                Duration(960.0)
            with Note(default_x=27.87, default_y=-538.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note(default_x=27.87, default_y=-478.53, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=96.81, default_y=-478.53, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=190.44, default_y=-478.53, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=259.01, default_y=-478.53, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='41', width=402.85):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(90.71)
                with StaffLayout(number=2):
                    StaffDistance(164.16)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Cédez -             -            -           -           -   //', default_y=35.4, font_weight='bold', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=58.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Words('dim. molto', default_y=54.8, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(print_object='no'):
                Rest()
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
            with Note(default_x=347.15, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='stop')
            with Backup():
                Duration(960.0)
            with Note(default_x=58.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=58.73, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(1)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(480.0)
                Voice('3')
                Type('quarter')
                Staff(1)
            with Note(default_x=238.96, default_y=-204.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=293.06, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('3')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=347.15, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('3')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(960.0)
            with Note(default_x=58.37, default_y=-189.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.05, default_y=-194.16):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.36, default_y=-199.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.67, default_y=-204.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=238.96, default_y=-204.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=293.06, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=347.15, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(960.0)
            with Note(default_x=58.37, default_y=-269.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='42', width=652.08):
            with Attributes():
                with Key():
                    Fifths(-5)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-66.6):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=67.96, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=95.37, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.78, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=150.18, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=187.59, default_y=-30.0, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(155.0)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(155.0)
            with Note(default_x=478.79, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
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
            with Note(default_x=509.82, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=469.93, relative_y=-45.49):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=540.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=568.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=595.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=623.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=175.59, default_y=-244.16):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=540.85, default_y=-204.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=568.25, default_y=-199.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=595.66, default_y=-204.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=623.07, default_y=-209.16):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-180.0)
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=67.6, default_y=-269.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=175.59, default_y=-234.16):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(17.0)
                Voice('7')
                Type('32nd')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=200.39, default_y=-209.16):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=221.21, default_y=-204.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=242.04, default_y=-194.16):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=262.86, default_y=-189.16):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=291.39, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=312.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=333.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=353.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=374.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=395.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=416.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=437.15, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=457.98, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(17.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(14)
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
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('8')
                Type('eighth')
                Staff(2)
            with Note(default_x=175.59, default_y=-234.16):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Tie(type='start')
                Voice('8')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=478.79, default_y=-219.16):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='stop')
                Voice('8')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='43', width=1054.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(244.5)
            with Note(default_x=121.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=160.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=200.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=239.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=279.19, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-963.25, relative_x=593.39, relative_y=-55.64):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Emporté   -          -            -    //      Cédez  -     -      // ', default_y=126.78, font_weight='bold', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=899.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=899.98, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-1013.89)
                Staff(1)
            with Note(default_x=935.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=935.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=978.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=978.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=1013.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=1013.92, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1, relative_x=-46.18)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=80.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Forward():
                Duration(480.0)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=116.63)
                Staff(1)
            with Note(default_x=804.87, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=850.27, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=892.68, default_y=-10.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=971.5, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=279.19, default_y=-299.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(420.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(180.0)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Forward():
                Duration(240.0)
            with Note(default_x=895.68, default_y=-299.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=895.68, default_y=-279.5):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=974.5, default_y=-289.5):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=974.5, default_y=-269.5):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=121.18, default_y=-349.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=121.54, default_y=-284.5):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('7')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=160.95, default_y=-279.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('7')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=200.36, default_y=-284.5):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('7')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=239.77, default_y=-289.5):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('7')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=291.05, default_y=-299.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('32nd')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=308.22, default_y=-289.5):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=327.71, default_y=-284.5):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=347.21, default_y=-279.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=366.7, default_y=-269.5):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=401.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=421.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=455.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=475.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=494.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=521.6, default_y=-289.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=541.1, default_y=-279.5):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=560.59, default_y=-274.5):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=581.41, default_y=-269.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=602.22, default_y=-259.5):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=637.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=656.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=676.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=697.11, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('7')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('7')
                Type('32nd')
                Dot()
                Dot()
                Dot()
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(2)
            with Forward():
                Duration(0.0)
            with Note(print_object='no'):
                Rest()
                Duration(101.0)
                Voice('7')
                Type('half')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('7')
                Type('32nd')
                with TimeModification():
                    ActualNotes(19)
                    NormalNotes(2)
                    NormalType('16th')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(1.0)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('8')
                Type('eighth')
                Staff(2)
            with Note(default_x=279.19, default_y=-339.5, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('8')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=724.87, default_y=-154.5, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('8')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', default_y=187.1, relative_y=20.0, font_style='italic', font_family='Times New Roman')
                Offset(-450.0)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('(rapide)', default_y=224.7, font_family='Times New Roman')
                Offset(-438.0)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('molto', default_y=217.48, font_style='italic', font_family='Times New Roman')
                Offset(-390.0)
                Staff(1)
            with Forward():
                Duration(240.0)
        with Measure(number='44', width=1054.93):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(99.77)
                with StaffLayout(number=2):
                    StaffDistance(992.74)
            with Note(default_x=124.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=124.68, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=194.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=194.42, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=272.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=272.77, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=83.85, relative_y=-52.64):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=342.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=342.51, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=416.55, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=416.55, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=416.55, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('molto', default_y=85.37, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=2, default_y=-1020.04)
                Staff(1)
            with Note(default_x=579.45, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=579.45, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=579.45, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=697.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=697.92, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=816.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=816.39, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=934.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=934.86, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-20.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=117.38, default_y=-10.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=265.47, default_y=10.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=404.69, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=404.69, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=404.69, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=579.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=579.45, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=579.45, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(240.0)
                Voice('4')
                Type('eighth')
                Staff(1)
            with Note(default_x=416.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('4')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=416.55, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('4')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=416.55, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('4')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('4')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=120.38, default_y=-1027.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=120.38, default_y=-1012.74):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=268.47, default_y=-1017.74):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=268.47, default_y=-1002.74):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=416.55, default_y=-1002.74, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='45', width=453.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(121.74)
                with StaffLayout(number=2):
                    StaffDistance(1352.54)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Trés retenu  -                -               -                -                -               -  //', default_y=83.94, font_weight='bold', font_family='Times New Roman')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-1288.43, relative_x=72.47, relative_y=-52.39):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-1335.82)
                Staff(1)
            with Note(default_x=124.68, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=124.68, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=146.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=199.17, default_y=-80.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=199.17, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('più', default_y=107.34, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=257.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=257.19, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-1289.08, relative_x=197.43, relative_y=-51.74):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=3, default_y=-1335.82)
                Staff(1)
            with Note(default_x=303.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=303.59, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=325.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=378.08, default_y=-80.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=378.08, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-190.0)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=3, relative_x=-50.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=117.38, default_y=-50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=172.0, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=296.29, default_y=-50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=350.91, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('3')
                Type('16th')
                Staff(1)
            with Note(default_x=188.17, default_y=-60.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('3')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('3')
                Type('16th')
                Staff(1)
            with Note(default_x=367.08, default_y=-60.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('3')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(480.0)
                Voice('4')
                Type('quarter')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(5)
                Duration(120.0)
                Voice('4')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(600.0)
            with Note(default_x=120.38, default_y=-1412.54):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=120.38, default_y=-1392.54):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=173.0, default_y=-1407.54):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=173.0, default_y=-1397.54):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=299.29, default_y=-1412.54):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=299.29, default_y=-1392.54):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=351.91, default_y=-1407.54):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=351.91, default_y=-1397.54):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=215.1, default_y=-1457.54):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=394.01, default_y=-1457.54):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='46', width=353.47):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-1285.73, relative_x=-3.5, relative_y=-55.09):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=19.3, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=19.3, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=41.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-1333.8)
                Staff(1)
            with Note(default_x=101.64, default_y=-80.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=101.64, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('più', default_y=107.34, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=154.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=154.02, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-1286.71, relative_x=115.84, relative_y=-53.08):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=201.1, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=201.1, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=3, default_y=-1334.79)
                Staff(1)
            with Note(default_x=223.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=276.44, default_y=-80.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=276.44, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-150.0)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=3, relative_x=-40.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=12.0, default_y=-50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=74.47, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=193.8, default_y=-50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=250.27, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(120.0)
                Voice('3')
                Type('16th')
                Staff(1)
            with Note(default_x=90.64, default_y=-60.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('3')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(120.0)
                Voice('3')
                Type('16th')
                Staff(1)
            with Note(default_x=266.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('3')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=15.0, default_y=-1412.54):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=15.0, default_y=-1392.54):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=68.47, default_y=-1407.54):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=68.47, default_y=-1397.54):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=196.8, default_y=-1412.54):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=196.8, default_y=-1392.54):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=250.27, default_y=-1407.54):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=250.27, default_y=-1397.54):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=111.25, default_y=-1457.54):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=293.05, default_y=-1457.54):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='47', width=247.97):
            with Note(default_x=28.28, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=28.28, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=28.28, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=12.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=12.12, default_y=-1407.54):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.12, default_y=-1397.54):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=56.38, default_y=-1457.54):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=144.91, default_y=-1457.54):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='48', width=1054.93):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(110.4)
            with Attributes():
                with Key():
                    Fifths(0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('(comme un très\n', default_y=24.6, font_family='Times New Roman', font_size='6.99956')
                    Words('léger glissando)')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('au Mouvement', default_y=40.4, font_weight='bold', font_family='Times New Roman')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=155.93, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=781.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(87.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Backup():
                Duration(3.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(65.0)
                Voice('2')
                Type('16th')
                Dot()
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=499.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=592.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=655.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=717.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(6.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=75.59, relative_y=-84.76):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=155.93, default_y=-160.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(65.0)
                Voice('5')
                Type('16th', size='cue')
                Dot()
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(type='start', placement='below', number=1)
            with Backup():
                Duration(2.0)
            with Note(default_x=235.71, default_y=-155.4):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=314.54, default_y=-145.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=376.89, default_y=-140.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=439.25, default_y=-135.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(print_object='no'):
                Rest()
                Duration(87.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(2.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=58.49, default_y=-215.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(720.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=955.89, default_y=-180.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=155.93, default_y=-180.4, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=753.36, default_y=-200.4, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
        with Measure(number='49', width=528.36):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(160.24)
                with StaffLayout(number=2):
                    StaffDistance(150.19)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=103.26, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=401.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(87.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Backup():
                Duration(3.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(65.0)
                Voice('2')
                Type('16th')
                Dot()
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=271.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=316.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=344.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=373.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(6.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=103.26, default_y=-190.19):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(65.0)
                Voice('5')
                Type('16th', size='cue')
                Dot()
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(type='start', placement='below', number=1)
            with Backup():
                Duration(2.0)
            with Note(default_x=140.97, default_y=-185.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=186.47, default_y=-180.19):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=215.11, default_y=-175.19):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=243.76, default_y=-170.19):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(print_object='no'):
                Rest()
                Duration(87.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(2.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=58.49, default_y=-255.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(720.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=482.0, default_y=-220.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=103.26, default_y=-220.19, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=370.82, default_y=-240.19, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
        with Measure(number='50', width=526.57):
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('doucement en dehors', default_y=61.38, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=75.54, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=413.88, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=469.42, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(5)
                Duration(87.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Backup():
                Duration(3.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(65.0)
                Voice('2')
                Type('16th')
                Dot()
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(87.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(3.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=75.54, default_y=-200.19):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th', size='cue')
                Dot()
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=118.39, default_y=-195.19):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=147.65, default_y=-185.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=191.7, default_y=-180.19):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=220.95, default_y=-175.19):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=250.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=293.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=323.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=352.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=381.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-255.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(720.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=469.42, default_y=-220.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=75.54, default_y=-220.19, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=375.88, default_y=-240.19, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
        with Measure(number='51', width=1054.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(227.63)
                with StaffLayout(number=2):
                    StaffDistance(160.46)
            with Note(default_x=61.11, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=830.71, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-70.0)
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-5.43)
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(87.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Backup():
                Duration(3.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(65.0)
                Voice('2')
                Type('16th')
                Dot()
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(87.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(3.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=172.42, default_y=-200.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th', size='cue')
                Dot()
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=256.31, default_y=-195.46):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=314.93, default_y=-190.46):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=393.32, default_y=-185.46):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=451.94, default_y=-180.46):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=510.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=598.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=656.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=715.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=774.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=61.11, default_y=-265.46):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(720.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=942.02, default_y=-230.46):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=172.42, default_y=-230.46, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=799.71, default_y=-250.46, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
        with Measure(number='52', width=538.89):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(111.47)
                with StaffLayout(number=2):
                    StaffDistance(160.92)
            with Note(default_x=61.11, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.91, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=431.69, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=484.49, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(5)
                Duration(87.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Backup():
                Duration(3.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(65.0)
                Voice('2')
                Type('16th')
                Dot()
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(87.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(3.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=113.91, default_y=-210.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th', size='cue')
                Dot()
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=154.74, default_y=-205.92):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=182.54, default_y=-195.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=225.27, default_y=-190.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=253.07, default_y=-185.92):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=280.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=322.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=350.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=378.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=405.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=61.11, default_y=-265.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(720.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=484.49, default_y=-230.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=113.91, default_y=-230.92, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=393.69, default_y=-250.92, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
        with Measure(number='53', width=516.04):
            with Note(default_x=20.0, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=132.61, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Tenuto()
            with Note(default_x=375.35, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=444.89, default_y=0.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                Rest()
                Duration(720.0)
                Voice('2')
                Type('quarter')
                Dot()
                Staff(1)
            with Note(default_x=461.06, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=135.61, default_y=-200.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th', size='cue')
                Dot()
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=177.64, default_y=-195.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=199.71, default_y=-190.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=221.78, default_y=-185.92):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=243.85, default_y=-180.92):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=265.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=289.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=311.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=333.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=355.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-265.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(720.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=444.89, default_y=-230.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=132.61, default_y=-230.92, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=349.35, default_y=-250.92, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
        with Measure(number='54', width=1054.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(268.93)
                with StaffLayout(number=2):
                    StaffDistance(418.73)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=24.15, relative_y=-29.4):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=78.15, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=90.01, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=78.15, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=273.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=285.05, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=273.18, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=2, default_y=-404.6)
                Staff(1)
            with Note(default_x=468.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=480.09, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=468.22, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=663.26, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=675.12, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=663.26, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=858.29, default_y=15.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=858.29, default_y=20.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=858.29, default_y=40.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-8.18)
                Staff(1)
            with Backup():
                Duration(1200.0)
            with Note(default_x=103.01, default_y=20.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=273.18, default_y=-483.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=273.18, default_y=-468.73):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=273.18, default_y=-453.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=468.22, default_y=-473.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=468.22, default_y=-453.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=468.22, default_y=-443.73):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=663.26, default_y=-468.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=663.26, default_y=-448.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=663.26, default_y=-438.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=858.29, default_y=-468.73, print_object='no'):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=858.29, default_y=-448.73, print_object='no'):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=858.29, default_y=-438.73, print_object='no'):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(1200.0)
            with Note(default_x=77.79, default_y=-523.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Forward():
                Duration(240.0)
        with Measure(number='55', width=413.39):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(75.65)
                with StaffLayout(number=2):
                    StaffDistance(739.99)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=94.31, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=322.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(87.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Backup():
                Duration(3.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(65.0)
                Voice('2')
                Type('16th')
                Dot()
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=221.6, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=258.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=281.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=302.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(6.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=94.31, default_y=-789.99):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(65.0)
                Voice('5')
                Type('16th', size='cue')
                Dot()
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(type='start', placement='below', number=1)
            with Backup():
                Duration(2.0)
            with Note(default_x=122.84, default_y=-784.99):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=160.35, default_y=-774.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=180.92, default_y=-769.99):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=201.74, default_y=-764.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(print_object='no'):
                Rest()
                Duration(87.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(2.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=58.49, default_y=-844.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(720.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=379.64, default_y=-809.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=94.31, default_y=-809.99, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=285.07, default_y=-829.99, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
        with Measure(number='56', width=270.65):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=4.94, relative_y=-51.12):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=67.65)
                Staff(1)
            with Note(default_x=20.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=32.59, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=20.72, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=79.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=91.65, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=79.79, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=2, default_y=-727.07)
                Staff(1)
            with Note(default_x=127.1, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=138.97, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=127.1, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=174.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=186.29, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=174.42, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=221.74, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=221.74, default_y=-10.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=221.74, default_y=15.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1, relative_x=-105.17)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-37.99)
                Staff(1)
            with Backup():
                Duration(1200.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=79.79, default_y=-799.99):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=79.79, default_y=-779.99):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=79.79, default_y=-769.99):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=127.1, default_y=-789.99):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=127.1, default_y=-769.99):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=127.1, default_y=-759.99):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=174.42, default_y=-779.99):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=174.42, default_y=-764.99):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=174.42, default_y=-754.99):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=221.74, default_y=-779.99, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=221.74, default_y=-764.99, print_object='no'):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=221.74, default_y=-754.99, print_object='no'):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(1200.0)
            with Note(default_x=20.36, default_y=-844.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(240.0)
        with Measure(number='57', width=370.89):
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=55.1, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=279.68, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(87.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Backup():
                Duration(3.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(65.0)
                Voice('2')
                Type('16th')
                Dot()
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=181.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=218.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=239.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=259.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(22.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(6.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=55.1, default_y=-779.99):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(65.0)
                Voice('5')
                Type('16th', size='cue')
                Dot()
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(type='start', placement='below', number=1)
            with Backup():
                Duration(2.0)
            with Note(default_x=82.91, default_y=-774.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.39, default_y=-769.99):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=141.21, default_y=-764.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=162.03, default_y=-759.99):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(22.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(print_object='no'):
                Rest()
                Duration(87.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(4)
                    NormalType('32nd')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(2.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-844.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(720.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=337.18, default_y=-809.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(960.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=55.1, default_y=-809.99, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=242.68, default_y=-829.99, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
        with Measure(number='58', width=332.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(243.29)
                with StaffLayout(number=2):
                    StaffDistance(80.83)
            with Direction(placement='above'):
                with DirectionType():
                    Words('più', default_y=92.63, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=71.22, relative_y=-38.25):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words("Très apaisé et très atténué jusqu'à la fin", default_y=116.43, font_weight='bold', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=78.15, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=90.01, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=78.15, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=166.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=177.92, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=166.05, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=204.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=204.3, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=242.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
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
                    Slur(type='stop', number=1)
            with Note(default_x=242.54, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=259.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=259.93, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=277.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=277.31, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=307.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=307.68, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(6)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=166.05, default_y=-145.83):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=166.05, default_y=-130.83):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=166.05, default_y=-115.83):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=204.3, default_y=-135.83):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=204.3, default_y=-115.83):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=204.3, default_y=-105.83):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=242.54, default_y=-130.83):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=242.54, default_y=-110.83):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=242.54, default_y=-100.83):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=78.15, default_y=-185.83):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='59', width=217.78):
            with Note(default_x=20.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=20.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=79.64, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=79.64, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=150.65, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=150.65, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=54.17, default_y=-140.83):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=54.17, default_y=-120.83):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=54.17, default_y=-110.83):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=150.65, default_y=-130.83):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=150.65, default_y=-110.83):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=150.65, default_y=-100.83):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=187.46, default_y=-120.83):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=187.46, default_y=-105.83):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=187.46, default_y=-95.83):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-185.83):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='60', width=279.06):
            with Note(default_x=25.83, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=37.7, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=25.83, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=112.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=124.6, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=112.74, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=150.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=150.96, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=189.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
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
            with Note(default_x=189.18, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=206.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=206.55, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=223.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=223.93, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=254.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=254.29, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(6)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=112.74, default_y=-145.83):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=112.74, default_y=-130.83):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=112.74, default_y=-115.83):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=150.96, default_y=-135.83):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=150.96, default_y=-115.83):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=150.96, default_y=-105.83):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=189.18, default_y=-130.83):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=189.18, default_y=-110.83):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=189.18, default_y=-100.83):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=25.83, default_y=-185.83):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='61', width=225.64):
            with Note(default_x=20.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=20.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=90.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=90.33, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=156.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=156.92, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=200.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=200.88, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=55.16, default_y=-140.83):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=55.16, default_y=-120.83):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=55.16, default_y=-110.83):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=90.33, default_y=-130.83):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=90.33, default_y=-110.83):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=90.33, default_y=-100.83):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=20.0, default_y=-185.83):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='62', width=1054.93):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(97.43)
            with Note(default_x=65.74, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=85.68, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=85.68, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=453.44, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=3.9, relative_y=10.0)
            with Note(default_x=473.38, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Fermata(None, type='upright', default_y=3.9, relative_y=10.0)
                    with Articulations():
                        Tenuto()
                        BreathMark(None)
            with Note(default_x=473.38, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=876.89, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
                    Fermata(None, type='upright', default_y=22.86, relative_y=10.0)
                    with Articulations():
                        Staccato()
                        BreathMark(None)
            with Note(default_x=876.89, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=906.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=906.06, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=968.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=968.41, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=65.74, default_y=-45.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(4)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=85.68, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note(default_x=101.85, default_y=-147.43):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(111.0)
                Voice('5')
                Type('16th', size='cue')
                Dot()
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Backup():
                Duration(3.0)
            with Note(default_x=146.55, default_y=-142.43):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=169.66, default_y=-132.43):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=186.83, default_y=-127.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=207.64, default_y=-122.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=337.0, default_y=-117.43):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=354.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=378.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=401.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=418.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=435.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(3.0)
            with Note(default_x=489.55, default_y=-147.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(111.0)
                Voice('5')
                Type('16th', size='cue')
                Dot()
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Backup():
                Duration(3.0)
            with Note(default_x=523.63, default_y=-137.43):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=556.84, default_y=-127.43):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=593.86, default_y=-117.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=627.08, default_y=-107.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=746.46, default_y=-97.43):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=763.62, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=785.65, default_y=-60.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=807.67, default_y=-40.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=829.7, default_y=-30.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=923.22, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(3.0)
            with Backup():
                Duration(960.0)
            with Note(default_x=70.68, default_y=-157.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=459.38, default_y=-157.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='below', number=1)
            with Backup():
                Duration(960.0)
            with Note(default_x=101.85, default_y=-182.43, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=319.83, default_y=-227.43, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=489.55, default_y=-182.43, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=731.27, default_y=-227.43, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='63', width=706.67):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(97.53)
            with Note(default_x=65.74, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=85.68, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=85.68, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=541.32, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Fermata(None, type='upright', relative_y=10.0)
                    with Articulations():
                        Tenuto()
                        BreathMark(None)
            with Note(default_x=541.32, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(960.0)
            with Note(default_x=65.74, default_y=-45.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(4)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=85.68, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(960.0)
            with Note(default_x=101.85, default_y=-147.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(111.0)
                Voice('5')
                Type('16th', size='cue')
                Dot()
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Backup():
                Duration(3.0)
            with Note(default_x=146.66, default_y=-142.53):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=185.04, default_y=-132.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=223.42, default_y=-127.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=261.8, default_y=-122.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=311.51, default_y=-117.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=349.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=388.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=426.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=465.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=503.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(37.0)
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(13)
                    NormalNotes(8)
                    NormalType('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Forward():
                Duration(3.0)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(960.0)
            with Note(default_x=70.68, default_y=-157.53):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='below', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(960.0)
            with Note(default_x=101.85, default_y=-187.53, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=501.32, default_y=-237.53, print_object='no', dynamics=0.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Staff(2)
        with Measure(number='64', width=348.26):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(960.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(960.0)
            with Note():
                Rest(measure='yes')
                Duration(960.0)
                Voice('5')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')