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
        CreditWords('BWV 0792', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Sinfonia 6', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Harp', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Harp')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(47)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=314.06):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(4)
                with Time():
                    Beats('9')
                    BeatType('8')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Presto', default_x=-35.3, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='12')
                Staff(1)
                Sound(tempo=184.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=128.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=148.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=188.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=208.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=229.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=249.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=269.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=289.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=128.15, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=249.1, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='2', width=229.64):
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=82.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=104.57, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=126.43, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=157.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=183.02, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=204.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=157.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=82.71, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=157.82, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='3', width=253.27):
            with Note(default_x=10.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=90.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=171.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=37.49, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=64.27, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=91.04, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=117.81, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=144.58, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=171.36, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=198.13, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=224.9, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='4', width=258.51):
            with Note(default_x=11.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=175.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=24.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=93.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=12.16, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.36, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=66.55, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=93.74, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=120.94, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.13, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=175.33, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=202.52, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=229.72, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='5', width=367.45):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(137.07)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=108.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=193.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=108.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=280.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=108.57, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=137.16, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=165.75, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=194.33, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=222.92, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=251.5, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=280.09, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=308.67, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=337.26, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='6', width=236.62):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=160.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=36.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=61.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=85.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=110.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=135.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=160.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=185.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=210.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=85.86, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=160.24, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='7', width=231.23):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=156.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=83.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=34.72, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.09, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=83.45, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=107.82, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=132.18, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=156.54, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.91, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=205.27, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='8', width=220.19):
            with Note(default_x=10.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=79.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=149.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=33.81, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=56.9, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=79.99, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=103.08, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=126.16, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=149.25, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=172.34, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.43, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='9', width=334.62):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(137.07)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=120.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=189.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=120.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=145.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=167.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=189.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=215.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=243.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=265.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=287.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=309.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=120.25, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=189.58, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=265.73, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='10', width=243.52):
            with Note(default_x=10.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=35.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=95.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=121.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=145.33, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=169.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=193.62, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=217.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=95.62, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=169.48, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='11', width=232.25):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=61.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=83.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=105.19, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=136.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=158.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=185.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=207.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=158.65, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='12', width=245.11):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=171.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=42.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=65.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=88.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=112.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=143.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=171.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=196.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=17.23, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=220.24, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=365.31):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(137.07)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=108.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=191.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=108.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=191.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=280.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=108.21, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=136.02, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.83, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=191.65, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=219.46, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=252.46, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=280.27, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=308.09, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=335.9, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='14', width=217.78):
            with Note(default_x=10.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=79.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=147.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=147.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=33.51, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=56.29, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=79.08, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=101.87, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=124.65, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=147.44, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=170.23, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=193.01, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='15', width=232.01):
            with Note(default_x=10.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=81.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=159.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=159.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=34.26, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=57.79, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=81.33, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=104.87, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.4, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=159.8, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=183.34, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.87, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='16', width=240.4):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=36.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=92.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=116.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=141.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=165.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=189.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=214.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=92.12, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='17', width=397.23):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(137.07)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=112.01, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=155.24, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=185.1, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=214.95, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=244.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=274.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=306.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=335.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=365.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=111.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=306.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=112.01, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=214.95, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=306.06, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='18', width=397.58):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=27.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=44.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=61.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=78.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=95.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=112.99, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=130.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=147.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=164.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=181.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=198.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=27.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=44.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=61.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=78.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=95.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=112.99, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=130.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=147.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=164.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=181.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=198.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=78.66, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=147.33, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=215.99, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=245.99, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=275.98, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=305.98, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=335.98, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=365.98, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='19', width=260.69):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=16.2, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.19, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=70.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=97.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=124.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=151.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=178.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=205.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=232.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=16.2, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=43.19, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=70.18, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=97.16, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=124.15, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.14, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=178.13, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='20', width=344.37):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(67.84)
            with Note(default_x=108.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=133.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=158.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=190.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=215.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=243.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=268.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=293.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=317.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=108.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=189.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=108.21, default_y=-107.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=190.3, default_y=-112.84):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=268.44, default_y=-97.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='21', width=231.92):
            with Note(default_x=10.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=59.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=87.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=111.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=134.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=158.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=183.31, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=158.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-117.84):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=87.23, default_y=-102.84):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='22', width=248.23):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=49.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=73.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=96.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=120.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=144.17, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=175.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=199.26, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=222.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-107.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=49.43, default_y=-112.84):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=73.11, default_y=-117.84):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=96.8, default_y=-122.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=120.49, default_y=-127.84):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=144.17, default_y=-132.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=175.57, default_y=-137.84):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=199.26, default_y=-132.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=222.94, default_y=-127.84):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='23', width=230.97):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=157.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=59.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=83.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=106.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=130.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=157.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=182.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=205.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-132.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='24', width=329.84):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=108.57, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=133.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=154.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=174.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=194.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=215.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=235.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=284.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=305.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=108.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=247.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=108.57, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='25', width=215.89):
            with Note(default_x=10.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=73.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=93.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=114.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=144.96, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=191.13, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=144.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=31.49, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=52.25, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=73.02, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=93.79, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=114.55, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=144.96, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=170.16, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.13, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='26', width=273.45):
            with Note(default_x=10.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=197.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(36.0)
            with Note(default_x=31.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=70.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=94.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=118.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=170.92, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=197.77, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=222.97, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=247.74, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=197.77, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='27', width=236.31):
            with Note(default_x=13.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=164.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=53.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=75.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=97.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=118.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=140.05, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=164.82, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=190.02, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=211.54, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=96.64, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='28', width=346.86):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=108.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=187.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=108.57, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=134.87, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.17, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=187.83, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=213.77, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=240.07, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=266.36, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=292.66, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=318.96, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=108.21, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=266.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='29', width=237.25):
            with Note(default_x=10.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=86.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=160.69, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=160.69, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.28, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=61.16, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=86.04, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=110.92, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=135.81, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=160.69, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=185.88, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.77, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='30', width=239.16):
            with Note(default_x=20.67, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=165.81, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=21.39, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=46.23, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=70.15, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=94.06, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=117.98, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=141.9, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=165.81, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=189.73, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=213.65, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=21.03, default_y=-170.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='31', width=232.22):
            with Note(default_x=13.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.89, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=61.98, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=86.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=110.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=134.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=158.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=182.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=85.71, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(1)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(1)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='32', width=329.53):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(78.21)
            with Note(default_x=108.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=254.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=108.93, default_y=-108.21):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=133.77, default_y=-118.21):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=157.22, default_y=-113.21):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=180.66, default_y=-108.21):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=205.43, default_y=-103.21):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=230.19, default_y=-98.21):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=254.96, default_y=-103.21):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=279.72, default_y=-98.21):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=304.49, default_y=-108.21):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=108.57, default_y=-163.21):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='33', width=193.68):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=32.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=50.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=69.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=94.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=113.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=150.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-113.21):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=69.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-173.21):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='34', width=123.39):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=13.4, relative_y=10.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-153.21):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='35', width=201.5):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=54.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=74.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=94.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=115.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=136.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=157.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=176.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-133.21):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.2, default_y=-128.21):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=54.86, default_y=-123.21):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=74.52, default_y=-118.21):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=94.18, default_y=-113.21):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=115.14, default_y=-108.21):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=136.11, default_y=-113.21):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=157.07, default_y=-108.21):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=176.73, default_y=-118.21):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-158.21):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='36', width=207.39):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=17.23, default_y=-123.21):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=17.23, default_y=-153.21):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.43, default_y=-143.21):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=61.1, default_y=-138.21):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=79.77, default_y=-133.21):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=98.44, default_y=-128.21):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=126.61, default_y=-123.21):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=145.28, default_y=-128.21):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=163.95, default_y=-123.21):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.63, default_y=-133.21):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='37', width=321.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(95.79)
            with Note(default_x=112.01, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.21, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=189.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=211.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=232.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=254.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=275.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=296.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=137.21, default_y=-145.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=168.61, default_y=-140.79):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=189.98, default_y=-135.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=211.35, default_y=-130.79):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=232.71, default_y=-125.79):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=254.08, default_y=-130.79):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=275.45, default_y=-125.79):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=296.82, default_y=-135.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=112.01, default_y=-155.79):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='38', width=319.52):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=27.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=45.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=81.02, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=109.43, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=127.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=183.66, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=212.07, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=233.03, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.79, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=268.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=289.51, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-140.79):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=109.43, default_y=-135.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=212.07, default_y=-130.79):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-150.79):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=109.43, default_y=-145.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=212.07, default_y=-140.79):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='39', width=189.71):
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=32.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=70.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=89.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.27, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=127.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-125.79):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=32.69, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=70.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=89.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=127.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-135.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='40', width=224.67):
            with Note(default_x=10.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=141.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=190.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=141.17, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=162.13, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=30.05, default_y=-130.79):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=49.98, default_y=-145.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=69.91, default_y=-140.79):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=89.84, default_y=-155.79):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=109.77, default_y=-150.79):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=141.17, default_y=-170.79):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=162.13, default_y=-165.79):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=190.3, default_y=-200.79):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='41', width=401.6):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(653.89)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=112.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=112.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=112.01, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')