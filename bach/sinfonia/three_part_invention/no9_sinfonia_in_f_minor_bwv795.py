with ScorePartwise(version='3.1'):
    with Identification():
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
        CreditWords('Sinfonia IX', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('BWV 795', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
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
        with Measure(number='1', width=366.28):
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
                    Fifths(-4)
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
                    Words('Andante', default_x=-37.42, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='12')
                Staff(1)
                Sound(tempo=96.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=159.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=188.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=217.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=276.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=305.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=335.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=129.8, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=188.52, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=247.24, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=305.96, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='2', width=299.96):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=48.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=82.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=117.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=151.87, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=186.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=229.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=263.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=14.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=82.94, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=151.87, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=186.34, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=229.43, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=263.9, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='3', width=389.25):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=50.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=88.89, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=127.27, default_y=-10.0):
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
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=249.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=287.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=326.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=88.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=190.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=287.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.12, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=127.27, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.19, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=172.64, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=190.08, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=221.48, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=249.4, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=326.16, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=359.73, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=632.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(132.92)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=194.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=248.39, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=302.26, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=390.96, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=444.83, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=484.0, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=523.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=577.04, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=116.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=248.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=390.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=444.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=577.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=116.18, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.35, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=194.53, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=302.26, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=341.43, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=366.2, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=390.96, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=444.83, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=523.17, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=577.04, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='5', width=422.99):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=63.45, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=111.1, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=158.74, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=206.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=301.69, default_y=0.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=332.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=361.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=391.61, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=158.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=206.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=254.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=301.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
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
                Duration(32.0)
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
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
        with Measure(number='6', width=606.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(132.92)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=116.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=268.9, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=299.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.99, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=360.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=482.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
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
            with Note(default_x=513.26, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=543.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=574.34, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=116.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=146.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=238.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=360.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=391.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=421.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=452.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=482.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='7', width=449.0):
            with Note(default_x=12.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=97.06, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=217.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=343.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=139.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=170.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=189.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=229.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=269.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=300.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=385.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=416.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=54.59, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=97.06, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=139.54, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=300.68, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=343.15, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=385.63, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='8', width=607.08):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(132.92)
                with StaffLayout(number=2):
                    StaffDistance(80.81)
            with Note(default_x=123.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=247.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=380.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=430.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=554.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=123.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=159.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=196.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=297.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=334.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=357.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=380.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=467.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=504.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=554.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=196.54, default_y=-115.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=247.08, default_y=-100.81):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=297.62, default_y=-95.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=380.33, default_y=-95.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=430.88, default_y=-100.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=467.64, default_y=-105.81):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=504.4, default_y=-110.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=554.94, default_y=-115.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='9', width=448.41):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=63.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=165.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=197.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=229.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=331.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=63.15, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=114.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=280.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=343.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=382.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-120.81):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=114.31, default_y=-120.81):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=229.4, default_y=-115.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=280.56, default_y=-120.81):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=382.87, default_y=-125.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=414.84, default_y=-130.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=555.03):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(132.92)
                with StaffLayout(number=2):
                    StaffDistance(65.81)
            with Note(default_x=107.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.86, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=212.33, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=264.81, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=382.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=435.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=487.84, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
                Duration(32.0)
            with Note(default_x=107.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=159.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=264.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=297.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=330.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=435.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=107.38, default_y=-110.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=159.86, default_y=-95.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=212.33, default_y=-90.81):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=330.41, default_y=-85.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=382.88, default_y=-90.81):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=487.84, default_y=-95.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=520.63, default_y=-100.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=500.46):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=49.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=116.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=150.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=196.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=230.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=251.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=272.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=305.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=339.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=431.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=465.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=83.01, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=150.22, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=196.42, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=339.24, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=385.45, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=431.65, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-95.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=150.22, default_y=-105.81):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=272.03, default_y=-110.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=385.45, default_y=-110.81):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=657.39):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.79)
            with Note(default_x=116.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=149.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=182.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=273.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=314.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=345.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=375.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=454.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=487.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=508.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=528.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=549.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=570.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=591.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=611.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=632.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(32.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=182.56, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=228.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=285.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=375.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
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
            with Note(default_x=421.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=454.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=487.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=570.4, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=116.18, default_y=-115.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=228.19, default_y=-115.79):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=375.41, default_y=-120.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=421.05, default_y=-125.79):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=487.43, default_y=-120.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=570.4, default_y=-155.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='13', width=398.1):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=54.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=93.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=132.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=262.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=301.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=340.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=93.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=206.1, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=301.3, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-140.79):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=132.16, default_y=-105.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.37, default_y=-100.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=181.33, default_y=-95.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=206.1, default_y=-95.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=234.3, default_y=-105.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=262.51, default_y=-100.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=340.08, default_y=-100.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=368.29, default_y=-110.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=499.72):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(98.69)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=175.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=215.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=254.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=319.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=359.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=388.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=418.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=458.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=116.18, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=215.13, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=319.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=359.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=418.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=458.42, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=116.18, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.05, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=175.42, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=254.83, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=283.71, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=301.76, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=319.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=359.51, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=418.71, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=458.42, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='15', width=266.15):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=75.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=106.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=169.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=201.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=232.98, default_y=-10.0):
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
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=75.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=138.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=201.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=106.71, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=138.27, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=169.84, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=232.98, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=289.62):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=46.61, default_y=-10.0):
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
            with Note(default_x=81.09, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=115.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=150.07, default_y=-5.0):
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
            with Note(default_x=184.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=219.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=81.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=150.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=184.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=219.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=253.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.12, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=46.61, default_y=-110.0):
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
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=115.58, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=150.07, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=184.56, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=253.53, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=540.12):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(98.69)
                with StaffLayout(number=2):
                    StaffDistance(65.79)
            with Note(default_x=116.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=221.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=327.35, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=432.93, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=168.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=221.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=274.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=380.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=432.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=485.73, default_y=-20.0):
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
            with Backup():
                Duration(32.0)
            with Note(default_x=116.18, default_y=-125.79):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=168.97, default_y=-130.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=274.56, default_y=-95.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=327.35, default_y=-120.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=380.14, default_y=-125.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=485.73, default_y=-90.79):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=515.37):
            with Note(default_x=12.12, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=117.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=255.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=384.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=64.67, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=332.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=384.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=437.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.12, default_y=-115.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=64.67, default_y=-120.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=169.78, default_y=-150.79):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=208.0, default_y=-145.79):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=231.89, default_y=-140.79):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=255.78, default_y=-140.79):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=294.0, default_y=-150.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=332.22, default_y=-145.79):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=437.33, default_y=-110.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=475.55, default_y=-120.79):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=622.37):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(98.69)
                with StaffLayout(number=2):
                    StaffDistance(65.79)
            with Note(default_x=118.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=258.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=389.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=437.2, default_y=-15.0):
                with Pitch():
                    Step('C')
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
            with Note(default_x=516.14, default_y=-15.0):
                with Pitch():
                    Step('C')
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
            with Note(default_x=568.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=194.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=246.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=299.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=384.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=449.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=478.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=516.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=568.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=118.58, default_y=-125.79):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=156.63, default_y=-135.79):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=194.67, default_y=-130.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=299.29, default_y=-125.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=337.34, default_y=-120.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=361.12, default_y=-115.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=384.89, default_y=-120.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=437.2, default_y=-115.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=516.14, default_y=-110.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=568.45, default_y=-145.79):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='20', width=433.13):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=61.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=160.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=190.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=221.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=320.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=110.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=221.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=271.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=369.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=400.68, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-130.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=61.36, default_y=-165.79):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=110.71, default_y=-125.79):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.07, default_y=-130.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=271.12, default_y=-130.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=320.48, default_y=-110.79):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=369.83, default_y=-115.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=405.34):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(98.69)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=116.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=148.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=181.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=214.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=292.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=327.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=360.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
                Duration(32.0)
            with Note(default_x=116.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=148.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=181.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=255.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=288.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=360.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=380.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=116.18, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=148.97, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=181.76, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=214.55, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=235.04, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=255.54, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=327.29, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=332.37):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=132.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=154.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=176.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=247.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=69.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=176.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=212.24, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=282.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=307.61, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.3, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=97.53, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.82, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=212.24, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=247.54, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=282.84, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='23', width=317.78):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=79.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=112.01, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=198.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=240.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=272.97, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
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
                Duration(32.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=79.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=162.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=194.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=272.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=293.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.87, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=112.01, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.06, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=162.42, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=240.9, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
        with Measure(number='24', width=410.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(98.69)
                with StaffLayout(number=2):
                    StaffDistance(72.46)
            with Note(default_x=107.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
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
            with Note(default_x=135.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=163.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=246.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=337.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=107.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=191.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=228.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=257.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=286.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=307.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=365.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=385.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=107.38, default_y=-132.46):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=135.29, default_y=-132.46):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.21, default_y=-122.46):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.37, default_y=-127.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=307.21, default_y=-127.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=337.57, default_y=-117.46):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=365.49, default_y=-122.46):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='25', width=357.46):
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=107.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat-flat')
                Stem('up')
                Staff(1)
            with Note(default_x=211.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=243.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=323.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=14.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.58, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=69.75, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=139.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=163.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=193.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=211.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=267.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=290.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=323.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=69.75, default_y=-117.46):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=107.56, default_y=-102.46):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=139.98, default_y=-97.46):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=211.09, default_y=-97.46):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=243.51, default_y=-102.46):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=267.08, default_y=-107.46):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=290.66, default_y=-112.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=323.08, default_y=-117.46):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='26', width=287.48):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=64.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=90.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=182.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=217.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=243.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=64.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=144.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=217.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-122.46):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=90.69, default_y=-132.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=109.76, default_y=-127.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=126.93, default_y=-122.46):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=144.09, default_y=-122.46):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=163.17, default_y=-132.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=182.24, default_y=-127.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=243.64, default_y=-127.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=262.72, default_y=-137.46):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=484.95):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(75.81)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=172.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=208.34, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=244.12, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
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
            with Note(default_x=319.67, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
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
            with Note(default_x=355.45, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=381.47, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=411.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=447.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=116.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=208.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=319.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=355.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=411.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
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
            with Note(default_x=447.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=116.18, default_y=-150.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.2, default_y=-155.81):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=172.56, default_y=-150.81):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=244.12, default_y=-110.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=270.14, default_y=-105.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=294.91, default_y=-100.81):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=319.67, default_y=-105.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=355.45, default_y=-100.81):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=411.8, default_y=-95.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=447.57, default_y=-130.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='28', width=274.05):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=76.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=143.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=207.79, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=44.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=76.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=175.47, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=207.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=240.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-115.81):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=108.98, default_y=-115.81):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=143.14, default_y=-105.81):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=175.47, default_y=-110.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=240.12, default_y=-110.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='29', width=296.5):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=85.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=155.35, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=190.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=225.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=260.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=50.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=85.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=120.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=155.35, default_y=-25.0):
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
            with Note(default_x=190.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=225.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-100.81):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.69, default_y=-105.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=120.46, default_y=-105.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=155.35, default_y=-95.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=190.23, default_y=-100.81):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=260.01, default_y=-95.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='30', width=366.12):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=149.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=179.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=210.2, default_y=-10.0):
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
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=272.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=303.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=333.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(32.0)
            with Note(default_x=118.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=179.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=242.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=303.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=118.58, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=149.12, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=210.2, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=242.37, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=272.91, default_y=-110.0):
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
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=333.98, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='31', width=355.68):
            with Note(default_x=12.0, default_y=-5.0):
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
            with Note(default_x=44.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=76.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=233.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=269.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=301.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=76.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=180.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=269.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=44.01, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=108.02, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.29, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=156.06, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=180.82, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=210.59, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=233.87, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=301.04, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=330.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=333.7):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=67.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=131.74, default_y=0.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=189.38, default_y=0.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=221.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=244.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=268.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=300.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=16.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=99.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=189.38, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=221.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=300.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=16.2, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.37, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=67.67, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=131.74, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.05, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=172.21, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=189.38, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=221.42, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=268.02, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=300.06, default_y=-149.73):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='33', width=466.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(105.79)
            with Note(default_x=107.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=216.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=242.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=260.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=277.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=305.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=331.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=404.7, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=438.27, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=107.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.76, default_y=-155.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=180.14, default_y=-145.79):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=216.52, default_y=-150.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=331.94, default_y=-150.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=368.32, default_y=-140.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=404.7, default_y=-145.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=107.38, default_y=-190.79):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=180.14, default_y=-155.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=277.31, default_y=-160.79):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=368.32, default_y=-160.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='34', width=463.29):
            with Note(default_x=16.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=77.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=162.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=203.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=223.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=253.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=326.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=357.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=430.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=77.94, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=120.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=174.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=253.34, default_y=-35.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=295.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=326.65, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=357.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=399.96, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=16.2, default_y=-165.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=120.38, default_y=-165.79):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=253.34, default_y=-170.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=295.78, default_y=-175.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=357.51, default_y=-170.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=399.96, default_y=-205.79):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='35', width=125.88):
            with Note(default_x=21.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(32.0)
            with Note(default_x=21.12, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('2')
                Type('whole')
                Accidental('natural')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=21.12, default_y=-190.79):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-64.0)
            with Barline(location='right'):
                BarStyle('light-heavy')