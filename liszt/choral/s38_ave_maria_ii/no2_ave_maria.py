with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Ave Maria S. 38')
    with Identification():
        Creator('Franz Liszt (1870)', type='composer')
        Rights('Copyright © 2017 by CPDL.  This edition can be fully distributed, duplicated, performed, and recorded.')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(7.00404)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1695.74)
            PageWidth(1199.64)
            with PageMargins(type='even'):
                LeftMargin(57.1099)
                RightMargin(57.1099)
                TopMargin(57.1099)
                BottomMargin(114.22)
            with PageMargins(type='odd'):
                LeftMargin(57.1099)
                RightMargin(57.1099)
                TopMargin(57.1099)
                BottomMargin(114.22)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='Times New Roman', font_size='11.9365')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Franz Liszt (1870)', default_x=1142.53, default_y=1586.63, justify='right', valign='bottom', font_family='Times New Roman', font_size='11.0064')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Ave Maria S. 38', default_x=599.82, default_y=1638.63, justify='center', valign='top', font_family='Times New Roman', font_size='22.0128')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Copyright © 2017 by CPDL.  This edition can be fully distributed, duplicated, performed, and recorded.', default_x=599.82, default_y=1581.52, justify='center', valign='top', font_family='Times New Roman')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Copyright © 2017 by CPDL.  This edition can be fully distributed, duplicated, performed, and recorded.', default_x=599.82, default_y=114.22, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Copyright © 2017 by CPDL.  This edition can be fully distributed, duplicated, performed, and recorded.', default_x=599.82, default_y=114.22, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Copyright © 2017 by CPDL.  This edition can be fully distributed, duplicated, performed, and recorded.', default_x=599.82, default_y=114.22, justify='center', valign='bottom', font_size='8')
    with Credit(page=4):
        CreditType('rights')
        CreditWords('Copyright © 2017 by CPDL.  This edition can be fully distributed, duplicated, performed, and recorded.', default_x=599.82, default_y=114.22, justify='center', valign='bottom', font_size='8')
    with Credit(page=5):
        CreditType('rights')
        CreditWords('Copyright © 2017 by CPDL.  This edition can be fully distributed, duplicated, performed, and recorded.', default_x=599.82, default_y=114.22, justify='center', valign='bottom', font_size='8')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('line')
        with ScorePart(id='P1'):
            PartName('Choir')
            PartAbbreviation('Choir')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Choir')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P2'):
            PartName('Organ')
            PartAbbreviation('Org.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Organ')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=154.62):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.17)
                        RightMargin(0.0)
                    TopSystemDistance(122.0)
                with StaffLayout(number=2):
                    StaffDistance(97.68)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(2)
                    Mode('major')
                with Time():
                    Beats('3')
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
                    with Metronome(parentheses='no', default_x=-36.36, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='2', width=58.47):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='3', width=58.47):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='4', width=58.47):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=7.5, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='5', width=81.12):
            with Note(default_x=11.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-70.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
            with Backup():
                Duration(6.0)
            with Note(default_x=11.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=11.72, default_y=-157.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=11.72, default_y=-137.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='6', width=109.28):
            with Note(default_x=23.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-70.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('ve')
            with Note(default_x=46.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=68.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-70.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ma')
            with Note(default_x=84.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=22.95, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=68.85, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-142.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=22.95, default_y=-137.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=68.85, default_y=-152.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=68.85, default_y=-137.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=69.9):
            with Note(default_x=10.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-70.11, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=45.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-147.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-137.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='8', width=79.04):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.37, default_y=-70.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('a,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=10.0, default_y=-147.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-137.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='9', width=64.43):
            with Note(default_x=17.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-70.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Backup():
                Duration(6.0)
            with Note(default_x=17.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.97, default_y=-157.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=17.97, default_y=-137.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='10', width=109.28):
            with Note(default_x=23.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-70.11, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
            with Note(default_x=46.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=68.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-70.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('a')
            with Note(default_x=84.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=22.95, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=68.85, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-142.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=22.95, default_y=-137.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=68.85, default_y=-152.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=68.85, default_y=-137.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=69.9):
            with Note(default_x=10.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-70.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ple')
            with Note(default_x=45.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-147.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-137.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='12', width=83.27):
            with Note(default_x=14.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.27, default_y=-70.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('na,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=14.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=14.23, default_y=-147.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=14.23, default_y=-137.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='13', width=542.1):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(85.14)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(131.21)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=91.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-77.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=91.21, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=367.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-77.66, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mi')
            with Note(default_x=367.84, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=91.21, default_y=-181.21):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=91.21, default_y=-166.21):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=367.84, default_y=-181.21):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=367.84, default_y=-161.21):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=91.21, default_y=-201.21):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=367.84, default_y=-206.21):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=458.18):
            with Note(default_x=19.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-77.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('nus')
            with Note(default_x=19.53, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=19.53, default_y=-166.21):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=19.53, default_y=-156.21):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=19.53, default_y=-211.21):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(4.0)
        with Measure(number='15', width=157.78):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(85.14)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(141.76)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-83.94)
                Staff(1)
            with Note(default_x=91.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-84.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('te')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=91.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=91.21, default_y=-176.76):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=131.33, default_y=-171.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=91.21, default_y=-186.76):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='16', width=98.31):
            with Note(default_x=23.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.49, default_y=-84.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('cum,')
            with Note(default_x=23.07, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.07, default_y=-166.76):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.07, default_y=-201.76):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(4.0)
        with Measure(number='17', width=110.79):
            with Note(default_x=10.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-84.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
            with Note(default_x=43.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=76.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-84.58, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ne')
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=76.37, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-191.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-181.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=76.37, default_y=-191.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.37, default_y=-181.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=119.82):
            with Note(default_x=17.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-84.58, relative_y=-30.0):
                    Syllabic('middle')
                    Text('di')
            with Note(default_x=44.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-84.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('cta')
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=83.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-186.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=17.59, default_y=-176.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=71.32, default_y=-186.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=71.32, default_y=-176.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='19', width=103.01):
            with Note(default_x=12.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.22, default_y=-84.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('tu')
            with Note(default_x=71.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.12, default_y=-191.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=12.12, default_y=-181.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=71.89, default_y=-196.76):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=71.89, default_y=-176.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='20', width=120.74):
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-84.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=13.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=48.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-84.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mu')
            with Note(default_x=48.91, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=84.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-84.58, relative_y=-30.0):
                    Syllabic('middle')
                    Text('li')
            with Note(default_x=84.02, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-206.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-171.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=48.91, default_y=-201.76):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=48.91, default_y=-176.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=84.02, default_y=-201.76):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=84.02, default_y=-181.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=82.13):
            with Note(default_x=17.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-84.58, relative_y=-30.0):
                    Syllabic('middle')
                    Text('e')
            with Note(default_x=17.59, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=52.9, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-84.58, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=52.9, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-196.76):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=17.59, default_y=-186.76):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=52.9, default_y=-196.76):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=52.9, default_y=-186.76):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=96.9):
            with Note(default_x=19.74, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-84.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('bus')
            with Note(default_x=19.74, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=70.11, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-84.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
            with Note(default_x=70.11, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=19.74, default_y=-196.76):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=19.74, default_y=-181.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=70.11, default_y=-196.76):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=70.11, default_y=-181.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=110.79):
            with Note(default_x=10.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-84.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
            with Note(default_x=43.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=76.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-84.58, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ne')
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=76.37, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-191.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-181.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=76.37, default_y=-191.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.37, default_y=-181.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='24', width=1000.28):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(85.14)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(93.43)
            with Note(default_x=103.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-67.57, relative_y=-30.0):
                    Syllabic('middle')
                    Text('di')
            with Note(default_x=401.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=700.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-67.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus')
            with Backup():
                Duration(6.0)
            with Note(default_x=103.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=712.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=103.25, default_y=-138.43):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=103.25, default_y=-128.43):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=700.32, default_y=-138.43):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=700.32, default_y=-128.43):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='25', width=187.28):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(85.14)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(152.1)
            with Note(default_x=92.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-92.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fru')
            with Note(default_x=122.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-80.19)
                Staff(1)
            with Note(default_x=150.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-92.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus')
            with Backup():
                Duration(6.0)
            with Note(default_x=91.79, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=150.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=92.15, default_y=-202.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=92.15, default_y=-192.1):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=122.05, default_y=-207.1):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=122.05, default_y=-187.1):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-75.0)
                Staff(2)
            with Note(default_x=150.76, default_y=-212.1):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=150.76, default_y=-187.1):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=104.86):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-92.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ven')
            with Note(default_x=42.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=71.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-92.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('tris')
            with Backup():
                Duration(6.0)
            with Note(default_x=13.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=71.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-182.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=42.88, default_y=-187.1):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2)
                Staff(2)
            with Note(default_x=71.97, default_y=-192.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.44, default_y=-217.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=71.97, default_y=-217.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='27', width=56.4):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=17.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-92.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tu')
            with Note(default_x=17.59, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-75.0)
                Staff(2)
            with Note(default_x=17.59, default_y=-217.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=17.59, default_y=-197.1):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='28', width=82.72):
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.12, default_y=-92.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('i,')
            with Note(default_x=17.23, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.23, default_y=-217.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=17.23, default_y=-197.1):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2)
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='29', width=55.03):
            with Direction(placement='above'):
                with DirectionType():
                    Words('a2', relative_y=20.0, font_family='Times New Roman', font_size='11.9365')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-92.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a2', default_y=8.95, relative_y=20.0, font_family='Times New Roman', font_size='11.9365')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=13.8, default_y=-182.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='30', width=54.88):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-182.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='31', width=54.93):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=12.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.95, default_y=-92.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('su.')
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=12.82, default_y=-202.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='32', width=53.89):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='33', width=65.65):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.68, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=20.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-92.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('San')
            with Backup():
                Duration(6.0)
            with Note(default_x=20.18, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=20.18, default_y=-202.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=20.18, default_y=-192.1):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='34', width=110.1):
            with Note(default_x=27.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-92.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('cta')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-87.69)
                Staff(1)
            with Note(default_x=48.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=69.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-92.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ma')
            with Note(default_x=85.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=27.31, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=69.67, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=14.72, default_y=-197.1):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=27.31, default_y=-192.1):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=69.67, default_y=-207.1):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=69.67, default_y=-192.1):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='35', width=68.43):
            with Note(default_x=29.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_y=-92.04, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Backup():
                Duration(6.0)
            with Note(default_x=29.62, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=29.62, default_y=-207.1):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=29.62, default_y=-197.1):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='36', width=106.1):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=50.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=9.37, default_y=-92.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('a,')
            with Backup():
                Duration(6.0)
            with Note(default_x=10.0, default_y=-202.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-192.1):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='37', width=138.59):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(85.14)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(119.05)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-87.69)
                Staff(1)
            with Note(default_x=95.01, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=95.01, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-75.0)
                Staff(2)
            with Note(default_x=95.01, default_y=-169.05):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=95.01, default_y=-159.05):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='38', width=114.86):
            with Note(default_x=27.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=3, default_y=-87.69)
                Staff(1)
            with Note(default_x=51.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=74.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-88.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=90.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=3)
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=27.31, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.43, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=14.72, default_y=-164.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=27.31, default_y=-159.05):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=74.43, default_y=-174.05):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=74.43, default_y=-159.05):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='39', width=83.22):
            with Note(default_x=29.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=29.62, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-88.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('De')
            with Backup():
                Duration(6.0)
            with Note(default_x=29.62, default_y=-174.05):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=29.62, default_y=-164.05):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='40', width=108.49):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=51.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=79.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=9.12, default_y=-88.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('i:')
            with Backup():
                Duration(6.0)
            with Note(default_x=10.0, default_y=-169.05):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-159.05):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='41', width=87.49):
            with Direction(placement='above'):
                with DirectionType():
                    Words('espressivo', default_y=8.43, relative_y=20.0, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=10.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-88.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
            with Note(default_x=10.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-159.05):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=56.98, default_y=-159.05):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-169.05):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='42', width=92.98):
            with Note(default_x=17.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-88.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=17.59, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=59.08, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-88.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('pro')
            with Note(default_x=59.08, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-169.05):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=17.59, default_y=-159.05):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=59.08, default_y=-164.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.08, default_y=-154.05):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='43', width=88.32):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-83.94)
                Staff(1)
            with Note(default_x=10.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_y=-88.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2)
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.49, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=10.36, default_y=-164.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
                with Lyric(number='2', default_y=-73.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=10.36, default_y=-154.05):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='44', width=96.16):
            with Note(default_x=17.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.94, default_y=-88.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note(default_x=64.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.95, default_y=-164.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=17.95, default_y=-154.05):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.22, default_y=-169.05):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=41.22, default_y=-159.05):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.48, default_y=-174.05):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Lyric(number='2', default_x=6.58, default_y=-73.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note(default_x=64.48, default_y=-159.05):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='45', width=96.82):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=17.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-88.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pec')
            with Note(default_x=17.59, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=64.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-88.33, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ca')
            with Note(default_x=64.57, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=17.59, default_y=-179.05):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=17.59, default_y=-159.05):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=64.57, default_y=-179.05):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.57, default_y=-159.05):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='46', width=93.35):
            with Note(default_x=17.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-88.33, relative_y=-30.0):
                    Syllabic('middle')
                    Text('to')
            with Note(default_x=17.59, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=64.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-88.33, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=64.11, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-179.05):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=17.59, default_y=-154.05):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=64.11, default_y=-179.05):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.11, default_y=-149.05):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='47', width=192.23):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(85.14)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(122.98)
            with Note(default_x=109.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-76.92, relative_y=-30.0):
                    Syllabic('end')
                    Text('bus')
                    Extend()
            with Note(default_x=109.25, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=109.25, default_y=-182.98):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=109.25, default_y=-152.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='48', width=92.62):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=10.0, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.0, default_y=-182.98):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=10.0, default_y=-157.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='49', width=109.0):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=26.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-76.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('nunc')
            with Note(default_x=26.38, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=26.38, default_y=-177.98):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=26.38, default_y=-157.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='50', width=96.92):
            with Note(default_x=11.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-76.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
            with Note(default_x=11.68, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=67.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-76.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=67.44, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=11.68, default_y=-177.98):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=11.68, default_y=-157.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=67.44, default_y=-177.98):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=67.44, default_y=-157.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='51', width=80.77):
            with Note(default_x=10.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-76.92, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ho')
            with Note(default_x=22.95, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-192.98):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=10.36, default_y=-157.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='52', width=84.44):
            with Note(default_x=16.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=16.87, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=57.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-76.92, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=57.19, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=16.87, default_y=-192.98):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=16.87, default_y=-157.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=57.19, default_y=-192.98):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=57.19, default_y=-172.98):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='53', width=98.17):
            with Note(default_x=15.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-76.92, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mor')
            with Note(default_x=15.2, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.2, default_y=-192.98):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=15.2, default_y=-172.98):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='54', width=79.11):
            with Note(default_x=13.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-76.92, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis')
            with Note(default_x=13.73, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.73, default_y=-157.98):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=53.12, default_y=-162.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.73, default_y=-192.98):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='55', width=90.41):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-77.31)
                Staff(1)
            with Note(default_x=17.59, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-76.92, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nos')
            with Note(default_x=17.59, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
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
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=17.59, default_y=-187.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=17.59, default_y=-167.98):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='56', width=76.61):
            with Note(default_x=20.67, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=20.67, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=20.67, default_y=-187.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=20.67, default_y=-167.98):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='57', width=164.29):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(85.14)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(119.51)
            with Note(default_x=103.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.36, default_y=-81.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('trae.')
            with Note(default_x=103.81, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=103.81, default_y=-184.51):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=103.81, default_y=-164.51):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='58', width=66.12):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='59', width=67.16):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=13.75, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.84, default_y=-189.51):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='60', width=67.16):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.84, default_y=-194.51):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='61', width=67.16):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=14.36, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-81.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=14.36, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=14.36, default_y=-164.51):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=14.36, default_y=-194.51):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='62', width=91.88):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-164.51):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-194.51):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='63', width=85.35):
            with Note(default_x=23.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.73, default_y=-81.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.12, default_y=-169.51):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Lyric(number='2', default_x=8.73, default_y=-81.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.12, default_y=-179.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='64', width=91.52):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='65', width=67.16):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='66', width=91.52):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='67', width=67.16):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='68', width=73.84):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=154.62):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(2)
                    Mode('major')
                with Time():
                    Beats('3')
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
                    Words('dolce', relative_y=20.0, font_weight='bold', font_style='italic', font_family='Times New Roman', font_size='11.4715')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=7.5, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=112.27, default_y=-382.68):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=58.47):
            with Note(default_x=13.8, default_y=-302.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=-287.68):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-357.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-382.68):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='3', width=58.47):
            with Note(default_x=13.8, default_y=-297.68):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-282.68):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-352.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-382.68):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='4', width=58.47):
            with Note(default_x=13.8, default_y=-292.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-277.68):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-382.68):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-347.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='5', width=81.12):
            with Note(default_x=12.08, default_y=-287.68):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=12.08, default_y=-277.68):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.08, default_y=-367.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=12.08, default_y=-347.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(4.0)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='6', width=109.28):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='7', width=69.9):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='8', width=79.04):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='9', width=64.43):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='10', width=109.28):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='11', width=69.9):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='12', width=83.27):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='13', width=542.1):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.06)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.21, default_y=-306.27):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=367.84, default_y=-311.27):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=91.21, default_y=-331.27):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=91.21, default_y=-396.27):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=367.84, default_y=-401.27):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=367.84, default_y=-391.27):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=458.18):
            with Note(default_x=19.53, default_y=-326.27):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=19.53, default_y=-316.27):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=19.53, default_y=-406.27):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=19.53, default_y=-386.27):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='15', width=157.78):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(68.02)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.21, default_y=-309.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=91.21, default_y=-334.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=131.33, default_y=-329.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=91.21, default_y=-389.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=131.33, default_y=-384.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=91.21, default_y=-399.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='16', width=98.31):
            with Note(default_x=23.07, default_y=-324.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=23.07, default_y=-314.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.07, default_y=-414.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=23.07, default_y=-379.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='17', width=110.79):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='18', width=119.82):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='19', width=103.01):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=42.0, default_y=-324.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=71.89, default_y=-319.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Forward():
                Duration(2.0)
            with Note(default_x=41.64, default_y=-334.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=42.0, default_y=-394.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=71.89, default_y=-389.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=42.0, default_y=-404.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=71.89, default_y=-409.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='20', width=120.74):
            with Note(default_x=13.8, default_y=-314.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=48.91, default_y=-309.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=84.02, default_y=-304.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-329.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=48.55, default_y=-324.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.44, default_y=-394.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-419.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=48.91, default_y=-414.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=84.02, default_y=-414.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=82.13):
            with Note(default_x=17.59, default_y=-329.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=17.59, default_y=-304.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=52.9, default_y=-334.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=52.9, default_y=-309.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-409.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=17.59, default_y=-399.78):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=96.9):
            with Note(default_x=19.74, default_y=-339.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=19.74, default_y=-314.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=19.74, default_y=-409.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=19.74, default_y=-394.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(4.0)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='23', width=110.79):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='24', width=1000.28):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='25', width=187.28):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(86.53)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-83.94)
                Staff(1)
            with Note(default_x=121.69, default_y=-327.1):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=122.05, default_y=-342.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=150.76, default_y=-337.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=121.69, default_y=-418.64):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=122.05, default_y=-438.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=150.76, default_y=-443.64):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=104.86):
            with Note(default_x=13.8, default_y=-322.1):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=42.88, default_y=-317.1):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=71.97, default_y=-312.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=13.44, default_y=-337.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.44, default_y=-423.64):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.44, default_y=-448.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='27', width=56.4):
            with Note(default_x=17.59, default_y=-312.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-337.1):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=17.59, default_y=-428.64):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-448.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='28', width=82.72):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='29', width=55.03):
            with Note(default_x=13.8, default_y=-312.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-413.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='30', width=54.88):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='31', width=54.93):
            with Note(default_x=12.82, default_y=-332.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.82, default_y=-433.64):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='32', width=53.89):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='33', width=65.65):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='34', width=110.1):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='35', width=68.43):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-41.73, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=29.62, default_y=-347.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=29.62, default_y=-317.1):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=29.62, default_y=-438.64):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=29.62, default_y=-428.64):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='36', width=106.1):
            with Note(default_x=10.0, default_y=-342.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=10.0, default_y=-322.1):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.0, default_y=-433.64):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-423.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='37', width=138.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(104.49)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='38', width=114.86):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='39', width=83.22):
            with Note(default_x=29.62, default_y=-353.54):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=29.62, default_y=-323.54):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=29.62, default_y=-423.54):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=29.62, default_y=-413.54):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='40', width=108.49):
            with Note(default_x=10.0, default_y=-348.54):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=10.0, default_y=-328.54):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.0, default_y=-418.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-408.54):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='41', width=87.49):
            with Note(default_x=10.36, default_y=-338.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=10.36, default_y=-313.54):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-408.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=56.98, default_y=-408.54):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-418.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='42', width=92.98):
            with Note(default_x=17.59, default_y=-343.54):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=17.59, default_y=-318.54):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=59.08, default_y=-348.54):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=59.08, default_y=-323.54):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-408.54):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.08, default_y=-403.54):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-418.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.08, default_y=-413.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='43', width=88.32):
            with Note(default_x=10.36, default_y=-323.54):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-348.54):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=57.49, default_y=-348.54):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-403.54):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-413.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='44', width=96.16):
            with Note(default_x=17.95, default_y=-323.54):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-348.54):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=64.48, default_y=-343.54):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.95, default_y=-403.54):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.22, default_y=-408.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=64.48, default_y=-413.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.95, default_y=-413.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.22, default_y=-418.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.48, default_y=-423.54):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='45', width=96.82):
            with Note(default_x=17.95, default_y=-338.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=17.95, default_y=-318.54):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.95, default_y=-428.54):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=17.95, default_y=-408.54):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='46', width=93.35):
            with Note(default_x=17.95, default_y=-338.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=17.95, default_y=-323.54):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.95, default_y=-428.54):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=17.95, default_y=-403.54):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='47', width=192.23):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=109.61, default_y=-302.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=109.61, default_y=-292.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=109.61, default_y=-392.98):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=109.61, default_y=-362.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='48', width=92.62):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='49', width=109.0):
            with Note(default_x=26.38, default_y=-307.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=26.38, default_y=-297.98):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=26.38, default_y=-387.98):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=26.38, default_y=-367.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='50', width=96.92):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='51', width=80.77):
            with Note(default_x=10.36, default_y=-307.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=22.95, default_y=-302.98):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=10.36, default_y=-402.98):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=10.36, default_y=-367.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='52', width=84.44):
            with Note(default_x=16.87, default_y=-312.98):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-302.98):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
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
            with Backup():
                Duration(6.0)
            with Note(default_x=16.87, default_y=-402.98):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=16.87, default_y=-367.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='53', width=98.17):
            with Note(default_x=15.56, default_y=-312.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=15.56, default_y=-302.98):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.56, default_y=-402.98):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.56, default_y=-367.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='54', width=79.11):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='55', width=90.41):
            with Note(default_x=17.59, default_y=-317.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=17.59, default_y=-302.98):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-397.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=17.59, default_y=-377.98):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='56', width=76.61):
            with Note(default_x=20.67, default_y=-317.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
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
            with Note(default_x=20.67, default_y=-307.98):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=20.67, default_y=-397.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=20.67, default_y=-377.98):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='57', width=164.29):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(97.16)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=103.81, default_y=-346.66):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=103.81, default_y=-336.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=103.81, default_y=-426.66):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=103.81, default_y=-406.66):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='58', width=66.12):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='59', width=67.16):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='60', width=67.16):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
        with Measure(number='61', width=67.16):
            with Note(default_x=14.36, default_y=-346.66):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=14.36, default_y=-336.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=14.36, default_y=-436.66):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=14.36, default_y=-406.66):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='62', width=91.88):
            with Note(default_x=14.16, default_y=-346.66):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=14.16, default_y=-336.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=14.16, default_y=-436.66):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=14.16, default_y=-406.66):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='63', width=85.35):
            with Note(default_x=23.12, default_y=-366.66):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=23.12, default_y=-356.66):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=23.12, default_y=-341.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.12, default_y=-456.66):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=23.12, default_y=-421.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='64', width=91.52):
            with Note(default_x=13.8, default_y=-366.66):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-356.66):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-341.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-456.66):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-421.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='65', width=67.16):
            with Note(default_x=13.8, default_y=-366.66):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-351.66):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-341.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-456.66):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-421.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='66', width=91.52):
            with Note(default_x=13.8, default_y=-366.66):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-351.66):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-341.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-456.66):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-421.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='67', width=67.16):
            with Note(default_x=13.8, default_y=-356.66):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-341.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-331.66):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-456.66):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-421.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='68', width=73.84):
            with Note(default_x=13.8, default_y=-356.66):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=13.8, default_y=-341.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-331.66):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-456.66):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', default_y=5.9, relative_y=10.0)
            with Note(default_x=13.8, default_y=-421.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')