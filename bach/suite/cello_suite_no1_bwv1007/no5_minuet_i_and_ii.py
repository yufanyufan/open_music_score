with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Cello Suite in G')
    with Identification():
        Creator('J. S. Bach', type='composer')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('http://musescore.com/user/1601076/scores/6200530')
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
        CreditWords('Cello Suite in G', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('(5th Movement - Minuet I and II)', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Violoncello')
            PartAbbreviation('Vc.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Violoncello')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=225.37):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-39.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=100.67, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=119.06, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=137.45, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=162.74, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=181.14, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=200.6, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='2', width=130.33):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=29.11, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=48.23, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=67.34, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=86.45, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=105.56, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='3', width=130.33):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=29.11, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=48.23, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=67.34, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=86.45, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=105.56, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=59.4):
            with Note(default_x=10.36, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=10.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=10.36, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=34.64, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=34.64, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=152.18):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=31.52, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=53.04, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=82.63, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=104.15, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.41, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='6', width=138.5):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=33.79, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=53.77, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=73.76, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.75, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=113.73, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='7', width=148.34):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=30.56, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.23, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=61.89, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=82.45, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=103.02, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.58, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=93.05):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=30.76, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=51.52, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=230.4):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    SystemDistance(96.38)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=107.98, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=126.72, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.46, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=171.23, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=189.97, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.64, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='10', width=132.43):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=29.53, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=49.06, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=68.6, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=88.13, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=107.66, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=153.16):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-79.22)
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=32.12, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=62.02, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=84.15, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=106.27, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=128.4, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=131.89):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.09, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=54.36, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=75.45, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=96.54, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='13', width=144.03):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-44.22, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.64, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=58.04, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=78.45, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=98.86, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=119.26, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='14', width=136.8):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=30.41, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=50.81, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.22, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.62, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.03, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='15', width=148.79):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.03, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=52.06, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.1, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.13, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=124.03, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=183.77):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    SystemDistance(96.38)
            with Note(default_x=83.41, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=120.74, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=139.87, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=159.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='17', width=149.8):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=30.2, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=50.4, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=78.17, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=98.37, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.03, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='18', width=141.15):
            with Note(default_x=14.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=34.48, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=54.95, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=75.43, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.91, default_y=-60.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=116.38, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='19', width=160.75):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.92, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=60.6, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=90.42, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=120.31, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=135.98, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=137.15):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=30.48, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=50.95, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=71.43, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=91.91, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=112.38, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=145.89):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=32.22, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=54.45, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=76.67, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=98.9, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=121.12, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='22', width=159.0):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=34.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=59.13, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=83.7, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=108.27, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=132.83, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='23', width=203.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(96.38)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=79.61, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=99.37, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=119.14, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=138.9, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=158.66, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=178.42, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=70.69):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=10.0, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=172.56):
            with Attributes():
                with Key():
                    Fifths(-1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=33.8, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=55.08, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=76.36, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=97.64, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=126.51, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=147.79, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='26', width=79.53):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=32.38, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=54.77, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='27', width=169.49):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.9, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=63.73, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=87.56, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=111.39, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=144.06, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='28', width=153.74):
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=35.12, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=56.44, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.76, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=107.66, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=128.98, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='29', width=148.76):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.28, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=52.56, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.84, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=102.71, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.99, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='30', width=79.53):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=32.38, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=54.77, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='31', width=248.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(96.38)
            with Note(default_x=78.78, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=108.67, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=135.7, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=162.72, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=189.74, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=220.2, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='32', width=147.56):
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=35.99, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=58.18, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=93.69, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=204.68):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-49.49, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=23.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=53.26, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=82.55, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=111.84, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=144.5, default_y=20.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=173.79, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='34', width=154.83):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.04, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=60.28, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=83.51, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=106.75, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=129.99, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=159.77):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=34.69, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=59.39, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=84.08, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=108.78, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=133.47, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='36', width=161.84):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=34.27, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=58.55, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=82.82, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=107.1, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=135.96, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='37', width=201.47):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    SystemDistance(96.38)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=78.78, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=98.36, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=117.95, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=137.54, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=157.12, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=176.71, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='38', width=143.27):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.66, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=57.12, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.58, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=98.04, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.5, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='39', width=169.16):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=46.47, default_y=20.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=70.68, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=94.9, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=119.12, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=143.34, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='40', width=114.68):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=28.41, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=46.81, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.22, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=83.63, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='41', width=151.88):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=14.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=35.06, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=56.12, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=84.99, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=106.05, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=127.11, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='42', width=149.17):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=37.16, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=58.11, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.38, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=114.04, default_y=20.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='43', width=147.88):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.06, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=59.93, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.99, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=102.05, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.11, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='44', width=207.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    SystemDistance(96.38)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=78.78, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=101.45, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=124.13, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=146.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=170.07, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='45', width=166.49):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=40.99, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=64.75, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=93.61, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=117.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.13, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='46', width=144.08):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.86, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=53.72, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=75.59, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=97.45, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=119.31, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='47', width=160.44):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.79, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=57.58, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.37, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=105.16, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=135.05, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='48', width=81.19):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='49', width=173.28):
            with Attributes():
                with Key():
                    Fifths(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=34.83, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=56.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.9, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=107.51, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=129.05, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.51, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='50', width=144.08):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.86, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=53.72, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=75.59, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=97.45, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='51', width=205.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    SystemDistance(102.27)
            with Note(default_x=79.61, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=99.89, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=120.17, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=140.44, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=160.72, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=181.0, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='52', width=65.22):
            with Note(default_x=10.36, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=10.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=10.36, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=40.46, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.46, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='53', width=153.63):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-49.05, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.85, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=53.7, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.75, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=105.6, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.86, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='54', width=144.32):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=34.95, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=56.1, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=77.25, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=98.4, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.55, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='55', width=154.16):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=32.02, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.68, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=63.35, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.36, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.38, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=129.4, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='56', width=82.1):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=33.5, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=57.0, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='57', width=136.15):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=29.59, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=49.18, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=76.12, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=95.72, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=111.38, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='58', width=136.15):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=30.28, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=50.55, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=70.83, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=91.11, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=111.38, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='59', width=228.3):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(96.38)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-79.16)
            with Note(default_x=79.61, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=103.05, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=132.95, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=156.39, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=179.83, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=203.27, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='60', width=137.42):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.29, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=55.56, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.85, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=100.15, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='61', width=149.56):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-44.16, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.74, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=60.26, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.77, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=103.28, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=124.79, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='62', width=142.33):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.51, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.02, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=74.54, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=96.05, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=117.56, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='63', width=154.32):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.41, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=54.83, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=77.24, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=99.66, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=129.56, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='64', width=114.96):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=51.52, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=70.86, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=90.19, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='65', width=150.61):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=30.38, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=50.77, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=78.79, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=99.17, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.84, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='66', width=222.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(96.38)
            with Note(default_x=88.41, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=110.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=132.32, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=154.27, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=176.23, default_y=-60.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=198.18, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='67', width=168.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=41.1, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=64.98, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=97.8, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.7, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=143.37, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='68', width=144.53):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.95, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=53.91, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=75.86, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=97.82, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=119.77, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='69', width=153.27):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=33.61, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=57.22, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=80.84, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=104.45, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=128.06, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='70', width=166.38):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=35.8, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=61.59, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=87.39, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=113.19, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=138.99, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='71', width=148.33):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=35.75, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=57.71, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=79.66, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=101.62, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=123.57, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='72', width=73.88):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=10.0, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')