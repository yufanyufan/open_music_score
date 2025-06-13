with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('Ped. 44')
        WorkTitle('COME, SWEET REST')
    with Identification():
        Creator('Virgil Fox', type='arranger')
        Creator('J.S.Bach', type='composer')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('/tmp/lg-374595084.tmp.pdf')
    with Defaults():
        with Scaling():
            Millimeters(7.112)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1571.0)
            PageWidth(1214.0)
            with PageMargins(type='both'):
                LeftMargin(80.0)
                RightMargin(80.0)
                TopMargin(80.0)
                BottomMargin(80.0)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='Serif', font_size='10')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J.S.Bach\n', default_x=1134.0, default_y=1341.0, justify='right', valign='bottom', font_size='12')
        CreditWords('\n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Virgil Fox\n', default_x=80.0, default_y=1341.0, justify='left', valign='bottom', font_size='12')
        CreditWords('\n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('title')
        CreditWords('Come Sweet Death', default_x=606.999, default_y=1491.0, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Komm Susser Tod', default_x=606.999, default_y=1434.76, justify='center', valign='top', font_size='14')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('brace')
        with ScorePart(id='P1'):
            PartName('Pipe Organ')
            PartAbbreviation('Org.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Pipe Organ')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(20)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=254.65):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.84)
                        RightMargin(0.0)
                    TopSystemDistance(220.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('3')
                    BeatType('4')
                Staves(3)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
                with Clef(number=3):
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.0, relative_x=126.86, relative_y=25.41):
                        BeatUnit('quarter')
                        PerMinute('40')
                Staff(1)
                Sound(tempo=40.0)
            with Note(default_x=119.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=119.83, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=157.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=157.24, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=194.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=218.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=229.88, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=119.83, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=119.83, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=157.24, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=157.24, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=194.64, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=194.64, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=119.83, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=156.88, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('down')
                Staff(3)
        with Measure(number='2', width=82.5):
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.36, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=12.36, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.36, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='3', width=162.44):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=7.9, relative_y=-28.23):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=56.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=56.37, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=96.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=123.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=135.48, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=56.37, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=96.95, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=85.08, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=96.95, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=56.01, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('down')
                Staff(3)
        with Measure(number='4', width=82.5):
            with Note(default_x=13.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=13.64, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.64, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=13.64, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.64, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='5', width=102.29):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=41.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=41.56, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=71.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=71.13, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=31.99)
                Staff(2)
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=12.0, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=41.56, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=71.13, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=71.13, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=41.56, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=71.13, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Tied(type='start')
        with Measure(number='6', width=130.59):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=51.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=51.0, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=89.99, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=89.99, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.0, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=51.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=51.0, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=89.99, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=89.99, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=51.0, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=89.99, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='7', width=135.69):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=27.67, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=52.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=52.2, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=97.69, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=97.69, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=52.2, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=74.94, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=97.69, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-245.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=52.2, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=97.69, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
                with Notations():
                    Tied(type='start')
        with Measure(number='8', width=82.5):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
                with Notations():
                    Tied(type='stop')
        with Measure(number='9', width=266.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.84)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(67.67)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=99.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=154.39, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=154.39, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=209.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=209.65, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=99.14, default_y=-122.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=99.14, default_y=-102.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=154.39, default_y=-122.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=154.39, default_y=-97.67):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=209.65, default_y=-127.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=209.65, default_y=-92.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=98.78, default_y=-227.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('down')
                Staff(3)
            with Note(default_x=209.65, default_y=-232.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='10', width=219.49):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=70.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=70.83, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=107.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=144.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=144.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=181.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=181.13, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-122.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=12.0, default_y=-112.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=70.83, default_y=-107.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=70.83, default_y=-92.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=144.36, default_y=-112.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-227.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=70.83, default_y=-257.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Note(default_x=144.36, default_y=-252.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='11', width=196.52):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=75.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=135.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-112.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-92.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=49.21)
                Staff(2)
            with Note(default_x=75.51, default_y=-117.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=116.77, default_y=-97.67):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(4)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=135.21, default_y=-112.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=135.21, default_y=-102.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.44, default_y=-232.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('down')
                Staff(3)
            with Note(default_x=135.21, default_y=-252.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Tie(type='start')
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Tied(type='start')
        with Measure(number='12', width=135.92):
            with Note(default_x=12.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.36, default_y=-112.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-102.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.36, default_y=-252.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(12.0)
                Tie(type='stop')
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
                with Notations():
                    Tied(type='stop')
        with Measure(number='13', width=214.72):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=14.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=14.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=75.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=75.27, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=136.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=136.53, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=174.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=174.82, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=14.0, default_y=-112.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=14.0, default_y=-102.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=75.27, default_y=-117.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=75.27, default_y=-102.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=136.53, default_y=-122.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=136.53, default_y=-112.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=14.0, default_y=-217.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=75.27, default_y=-222.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=136.53, default_y=-227.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(3)
        with Measure(number='14', width=227.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.84)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(77.67)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=98.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=98.78, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=139.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=151.66, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=180.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=195.72, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=206.69, default_y=-20.0):
                Grace()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=98.78, default_y=-127.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=98.78, default_y=-107.67):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.79, default_y=-102.67):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=180.8, default_y=-107.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=98.78, default_y=-232.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=139.79, default_y=-252.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=180.8, default_y=-247.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='15', width=110.19):
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-107.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=16.16, default_y=-267.67):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=38.43, default_y=-232.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=54.09, default_y=-227.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=69.76, default_y=-232.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=85.43, default_y=-237.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='16', width=165.29):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=36.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=36.7, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=57.6, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=57.6, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=86.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=86.43, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=111.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=111.7, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=140.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=140.53, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=17.94, relative_y=32.43):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=15.8, default_y=-107.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=57.24, default_y=-112.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-242.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(3)
            with Note(default_x=86.43, default_y=-247.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=111.7, default_y=-242.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=140.53, default_y=-252.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='17', width=89.91):
            with Note(default_x=12.72, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=12.72, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=33.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=49.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=49.48, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=65.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=65.15, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.36, default_y=-112.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=65.15, default_y=-117.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.72, default_y=-237.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=33.81, default_y=-247.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=65.15, default_y=-232.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='18', width=114.92):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.36, default_y=-112.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.72, default_y=-252.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=35.56, default_y=-217.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=55.02, default_y=-212.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=74.49, default_y=-217.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=90.16, default_y=-222.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='19', width=142.21):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=42.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=42.87, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=71.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=71.7, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=88.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=88.62, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=117.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=117.44, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-122.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-97.67):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=39.67)
                Staff(2)
            with Note(default_x=42.87, default_y=-132.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=42.87, default_y=-112.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=88.62, default_y=-122.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=88.62, default_y=-97.67):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-227.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=42.87, default_y=-237.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=88.62, default_y=-227.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='20', width=183.13):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=44.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=71.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=100.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=127.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=154.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=154.51, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-117.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-97.67):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=44.63, default_y=-122.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=44.63, default_y=-97.67):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=71.64, default_y=-127.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=71.64, default_y=-92.67):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=100.47, default_y=-132.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=100.47, default_y=-92.67):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=127.49, default_y=-127.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=127.49, default_y=-102.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=154.51, default_y=-127.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=154.51, default_y=-107.67):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-222.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=44.63, default_y=-227.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=71.64, default_y=-232.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=100.47, default_y=-237.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=127.49, default_y=-232.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=223.87):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.84)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(66.6)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=107.58, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=107.58, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=139.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=139.05, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=107.58, default_y=-116.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=107.58, default_y=-101.6):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=139.41, default_y=-121.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=139.41, default_y=-96.6):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=159.31, default_y=-126.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=179.21, default_y=-121.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=199.1, default_y=-131.6):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=199.1, default_y=-96.6):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=107.58, default_y=-221.6):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=139.41, default_y=-226.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=159.31, default_y=-231.6):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=179.21, default_y=-226.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=199.1, default_y=-236.6):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='22', width=214.56):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=48.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=48.23, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=80.65, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=80.65, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=113.08, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=113.08, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=145.5, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=145.5, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=177.93, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=189.79, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-116.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-96.6):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=80.65, default_y=-111.6):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=145.5, default_y=-146.6):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=145.5, default_y=-116.6):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-256.6):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=80.29, default_y=-251.6):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
        with Measure(number='23', width=83.72):
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-131.6):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.16, default_y=-236.6):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=36.09, default_y=-226.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=56.01, default_y=-216.6):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='24', width=124.39):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=47.73, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=79.67, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.63, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=20.94, relative_y=30.6):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Note(default_x=15.8, default_y=-146.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-136.6):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=47.73, default_y=-141.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=79.67, default_y=-141.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=79.67, default_y=-126.6):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-236.6):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=47.37, default_y=-231.6):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('down')
                Staff(3)
        with Measure(number='25', width=117.73):
            with Note(default_x=12.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.72, default_y=-146.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=12.72, default_y=-136.6):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=12.72, default_y=-126.6):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=40.63, default_y=-146.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=58.08, default_y=-141.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=75.52, default_y=-136.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=92.96, default_y=-146.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=92.96, default_y=-126.6):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.36, default_y=-226.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='26', width=149.89):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=54.06, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=92.31, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=124.38, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-146.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-136.6):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-121.6):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=54.06, default_y=-141.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=54.06, default_y=-131.6):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=54.06, default_y=-121.6):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=92.31, default_y=-141.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=92.31, default_y=-131.6):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=92.31, default_y=-116.6):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-236.6):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=53.7, default_y=-221.6):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('down')
                Staff(3)
        with Measure(number='27', width=119.01):
            with Note(default_x=13.64, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=14.0, default_y=-136.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=14.0, default_y=-126.6):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=14.0, default_y=-116.6):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=41.91, default_y=-116.6):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=59.35, default_y=-121.6):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=76.8, default_y=-126.6):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=94.24, default_y=-136.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=94.24, default_y=-116.6):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=13.64, default_y=-216.6):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='28', width=185.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.84)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(82.21)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=102.58, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=129.79, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=157.01, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=102.58, default_y=-152.21):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=129.79, default_y=-157.21):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=157.01, default_y=-162.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=157.01, default_y=-152.21):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=102.58, default_y=-242.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=129.79, default_y=-247.21):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=157.01, default_y=-252.21):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Tied(type='start')
        with Measure(number='29', width=97.22):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=70.3, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.16, default_y=-162.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=16.16, default_y=-147.21):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=41.48, default_y=-157.21):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=41.48, default_y=-142.21):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=70.3, default_y=-162.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=70.3, default_y=-152.21):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=70.3, default_y=-142.21):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=16.16, default_y=-252.21):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.48, default_y=-247.21):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=70.3, default_y=-242.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='30', width=110.62):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=83.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.72, default_y=-162.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=12.72, default_y=-137.21):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=38.43, default_y=-167.21):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=38.43, default_y=-142.21):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=67.25, default_y=-167.21):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=67.25, default_y=-147.21):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=83.32, default_y=-162.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=83.32, default_y=-152.21):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.72, default_y=-262.21):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=38.43, default_y=-257.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=83.32, default_y=-242.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
                with Notations():
                    Tied(type='start')
        with Measure(number='31', width=59.12):
            with Note(default_x=12.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.36, default_y=-162.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-152.21):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.36, default_y=-242.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
                with Notations():
                    Tied(type='stop')
        with Measure(number='32', width=108.68):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=46.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=76.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-177.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-152.21):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=46.23, default_y=-172.21):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=46.23, default_y=-157.21):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=76.65, default_y=-167.21):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=76.65, default_y=-157.21):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.44, default_y=-242.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('down')
                Staff(3)
            with Note(default_x=76.65, default_y=-247.21):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='33', width=166.21):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=79.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=100.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=120.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=141.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-187.21):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-152.21):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=79.38, default_y=-122.21):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=79.38, default_y=-107.21):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=120.76, default_y=-127.21):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=120.76, default_y=-117.21):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=120.76, default_y=-107.21):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-242.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=79.38, default_y=-272.21):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Note(default_x=120.76, default_y=-267.21):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='34', width=119.72):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=49.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=84.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-127.21):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-107.21):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=49.03, default_y=-132.21):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=66.44, default_y=-112.21):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(4)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=84.89, default_y=-127.21):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=84.89, default_y=-117.21):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.44, default_y=-247.21):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('down')
                Staff(3)
            with Note(default_x=84.89, default_y=-267.21):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Tie(type='start')
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Tied(type='start')
        with Measure(number='35', width=59.12):
            with Note(default_x=12.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.36, default_y=-127.21):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-117.21):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.36, default_y=-267.21):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(12.0)
                Tie(type='stop')
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
                with Notations():
                    Tied(type='stop')
        with Measure(number='36', width=126.65):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=4.93, relative_y=-29.64):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=17.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=47.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=77.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=101.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.8, default_y=-117.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=17.8, default_y=-102.21):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=47.42, default_y=-117.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.42, default_y=-97.21):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.04, default_y=-127.21):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.04, default_y=-92.21):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.8, default_y=-232.21):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=47.42, default_y=-237.21):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=77.04, default_y=-242.21):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(3)
        with Measure(number='37', width=238.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.84)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=102.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=137.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=197.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=213.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=102.58, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=102.58, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=137.51, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=137.51, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=172.44, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=172.44, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=102.58, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=137.51, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=172.44, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='38', width=120.03):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.8, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=16.16, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=43.68, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=60.87, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=78.07, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=95.26, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='39', width=146.84):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=56.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=101.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=56.3, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=56.3, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=76.55, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=101.82, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=122.07, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(3)
            with Note(default_x=76.55, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=101.82, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=122.07, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='40', width=103.19):
            with Note(default_x=16.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=42.45, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=58.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=75.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=75.3, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=75.3, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.16, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=42.45, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=75.3, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='41', width=128.2):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.16, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=45.91, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=65.38, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=84.84, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=103.43, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='42', width=130.02):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=40.63, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=58.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=76.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=105.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=12.0, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=40.63, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=58.53, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=76.42, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=76.42, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=105.25, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=105.25, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=40.63, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=76.42, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='43', width=166.39):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=62.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=85.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=118.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=141.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=39.19, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=62.57, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=85.96, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=118.02, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=141.41, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=141.41, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=39.19, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=62.57, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=85.96, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=118.02, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
                with Notations():
                    Tied(type='start')
        with Measure(number='44', width=296.4):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.84)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=111.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=111.38, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=111.38, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=111.38, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=163.42, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=163.42, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=163.42, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=111.38, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=163.78, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=196.54, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=229.29, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=262.05, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='45', width=213.75):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=48.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=81.25, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=146.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=179.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=27.67, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=81.25, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=81.25, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=146.7, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=146.7, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=158.57, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=80.89, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
        with Measure(number='46', width=176.68):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.16, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=67.47, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=118.77, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='47', width=206.38):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=27.67, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=78.79, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=78.79, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=78.79, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=141.79, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=141.79, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=141.79, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.3, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=78.79, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=110.29, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=141.79, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=173.28, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=78.43, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
        with Measure(number='48', width=139.95):
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-heavy')