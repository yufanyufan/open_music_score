with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Siciliana')
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
        CreditWords('Siciliana', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('brace')
        with ScorePart(id='P1'):
            PartName('Varhany')
            PartAbbreviation('Varh.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Varhany')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(20)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=170.56):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
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
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=101.43, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=123.61, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=145.79, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('9')
                Staff(3)
        with Measure(number='2', width=89.08):
            with Direction(placement='above'):
                with DirectionType():
                    Words('cantabile lamentando', relative_y=20.0)
                Staff(1)
            with Note(default_x=10.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=43.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=60.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='3', width=79.84):
            with Note(default_x=10.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=32.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=55.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='4', width=92.89):
            with Note(default_x=23.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=57.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=22.95, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.95, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='5', width=107.36):
            with Note(default_x=17.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=52.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=77.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.59, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=17.59, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.59, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(3)
        with Measure(number='6', width=79.48):
            with Note(default_x=10.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=32.54, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=54.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-245.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
        with Measure(number='7', width=100.13):
            with Note(default_x=10.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=45.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=70.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='8', width=88.39):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=79.84):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=10.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=32.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=55.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='10', width=89.08):
            with Note(default_x=10.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=43.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=60.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='11', width=79.84):
            with Note(default_x=10.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=32.9, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=55.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='12', width=150.3):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=80.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=98.15, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=109.12, default_y=-20.0):
                Grace()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=120.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=80.38, default_y=-140.0):
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
            with Note(default_x=80.38, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='13', width=75.94):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=10.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=30.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=51.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-100.0):
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
            with Note(default_x=10.36, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
        with Measure(number='14', width=79.94):
            with Note(default_x=14.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=34.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=55.17, default_y=-35.0):
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
            with Note(default_x=14.36, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=14.36, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(3)
        with Measure(number='15', width=90.35):
            with Note(default_x=14.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=32.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=50.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
                        BreathMark(None)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
        with Measure(number='16', width=75.94):
            with Note(default_x=10.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=30.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=51.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-100.0):
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
            with Note(default_x=10.36, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
        with Measure(number='17', width=88.61):
            with Note(default_x=14.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=45.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=61.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
        with Measure(number='18', width=79.38):
            with Note(default_x=14.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=34.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=54.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
        with Measure(number='19', width=94.58):
            with Note(default_x=23.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=55.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=22.95, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=22.95, default_y=-100.0):
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
            with Note(default_x=22.95, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='20', width=85.17):
            with Note(default_x=10.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=41.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=57.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-100.0):
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
            with Note(default_x=10.36, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='21', width=79.38):
            with Note(default_x=14.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=34.39, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=54.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-100.0):
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
            with Note(default_x=13.8, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
        with Measure(number='22', width=71.75):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=41.38, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
            with Note(default_x=41.38, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='23', width=85.17):
            with Note(default_x=10.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=41.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=57.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='24', width=225.68):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=80.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=128.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=176.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=80.38, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=80.38, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=80.38, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='25', width=174.31):
            with Note(default_x=23.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=95.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=22.95, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.95, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='26', width=162.89):
            with Note(default_x=17.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=65.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=113.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.59, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=17.59, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.59, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(3)
        with Measure(number='27', width=155.66):
            with Note(default_x=10.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=58.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=106.28, default_y=-35.0):
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
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('down')
                Staff(3)
        with Measure(number='28', width=195.81):
            with Note(default_x=10.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=62.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=109.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=161.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-245.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
        with Measure(number='29', width=142.14):
            with Note(default_x=13.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('half')
                Dot()
                Stem('up')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-heavy')