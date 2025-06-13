with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Бах. Энгармонизм. Клавир')
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
        CreditWords("Bach's enharmonic modulation", default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Mass in B minor, BWV 232, Credo, "Et expecto resurrectionem mortuorum"', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(49)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=437.71):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(121.38)
                with StaffLayout(number=4):
                    StaffDistance(65.0)
                with StaffLayout(number=5):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(3)
                with Time():
                    Beats('4')
                    BeatType('4')
                Staves(5)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('G')
                    Line(2)
                with Clef(number=3):
                    Sign('G')
                    Line(2)
                with Clef(number=4):
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
                with Clef(number=5):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-51.36, relative_x=-79.01, relative_y=27.81):
                        BeatUnit('quarter')
                        PerMinute('70')
                Staff(1)
                Sound(tempo=70.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Leading-tone seventh chord\n', relative_x=-49.49, relative_y=44.22)
                    Words('to dominant in g minor.\n')
                    Words(None)
                Staff(1)
            with Note(default_x=134.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(4.0)
            with Note(default_x=134.31, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Backup():
                Duration(4.0)
            with Note(default_x=137.63, default_y=-321.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('9')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(3)
                with Notations():
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=212.25, default_y=-326.38):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=286.87, default_y=-331.38):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('9')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(3)
            with Note(default_x=361.49, default_y=-326.38):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Backup():
                Duration(4.0)
            with Note(default_x=137.27, default_y=-411.38):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('13')
                Type('half')
                Stem('up')
                Staff(4)
                with Notations():
                    Slur(type='start', placement='above', number=4)
            with Note(default_x=286.51, default_y=-376.38):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('13')
                Type('half')
                Stem('down')
                Staff(4)
            with Backup():
                Duration(4.0)
            with Note(default_x=134.31, default_y=-501.38):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('17')
                Type('whole')
                Accidental('sharp')
                Staff(5)
                with Notations():
                    Slur(type='start', placement='above', number=5)
        with Measure(number='2', width=392.27):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Cadential 6-4 chord\n', default_y=3.0, relative_x=-10.42, relative_y=36.4)
                    Words('in g minor \n')
                    Words(None)
                Staff(1)
            with Note(default_x=19.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=19.52, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
            with Backup():
                Duration(4.0)
            with Note(default_x=22.84, default_y=-321.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('9')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(3)
            with Note(default_x=125.02, default_y=-331.38):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('9')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Leading-tone seventh chord\n', default_y=24.8, relative_x=-65.99, relative_y=77.18)
                    Words('to dominant in g minor\n')
                    Words('at organ point\n')
                    Words('\n')
                    Words(None)
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=22.04, relative_x=4.34)
                Staff(3)
            with Note(default_x=226.83, default_y=-306.38):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none', relative_x=-146.74)
                Staff(3)
            with Backup():
                Duration(4.0)
            with Note(default_x=22.48, default_y=-381.38):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('13')
                Type('half')
                Stem('down')
                Staff(4)
            with Note(default_x=226.83, default_y=-386.38):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('13')
                Type('half')
                Stem('down')
                Staff(4)
            with Backup():
                Duration(4.0)
            with Note(default_x=19.52, default_y=-496.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('17')
                Type('whole')
                Staff(5)
        with Measure(number='3', width=241.32):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Dominant\n', relative_x=29.25, relative_y=40.39)
                    Words('in g minor\n')
                    Words(None)
                Staff(1)
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=126.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=13.8, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=126.58, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(4.0)
            with Note(default_x=13.8, default_y=-326.38):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
            with Note(default_x=126.58, default_y=-301.38):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
            with Backup():
                Duration(4.0)
            with Note(default_x=13.8, default_y=-381.38):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('13')
                Type('half')
                Stem('down')
                Staff(4)
            with Note(default_x=126.58, default_y=-381.38):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('13')
                Type('half')
                Stem('down')
                Staff(4)
            with Backup():
                Duration(4.0)
            with Note(default_x=13.8, default_y=-496.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('17')
                Type('half')
                Stem('down')
                Staff(5)
            with Note(default_x=126.58, default_y=-461.38):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('17')
                Type('half')
                Stem('down')
                Staff(5)
        with Measure(number='4', width=744.34):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
                with StaffLayout(number=4):
                    StaffDistance(65.0)
                with StaffLayout(number=5):
                    StaffDistance(65.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Leading-tone 6-4-3 chord\n', relative_x=-5.21, relative_y=58.1)
                    Words('to tonic in g minor.\n')
                    Words(None)
                Staff(1)
            with Note(default_x=101.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Leading-tone 6-5 chord\n', relative_x=33.86, relative_y=61.23)
                    Words('to dominant in e♭ minor.\n')
                    Words(None)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('=', relative_x=-29.52, relative_y=37.37, font_size='30')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=30.03, relative_x=-122.43)
                Staff(1)
            with Note(default_x=386.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none', relative_x=-367.29)
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=101.21, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=386.17, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(4.0)
            with Note(default_x=101.21, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Words('Enharmonic equality', default_y=-40.0, relative_x=63.38, relative_y=-16.41)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=-45.43, relative_x=9.55)
                Staff(3)
            with Note(default_x=386.17, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('9')
                Type('half')
                Stem('up')
                Notehead('normal', color='#FF00FF')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none', relative_x=-291.74)
                Staff(3)
            with Backup():
                Duration(4.0)
            with Note(default_x=101.21, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('13')
                Type('half')
                Stem('down')
                Staff(4)
            with Note(default_x=386.54, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('13')
                Type('quarter')
                Stem('up')
                Staff(4)
            with Note(default_x=564.64, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('13')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(4)
            with Backup():
                Duration(4.0)
            with Note(default_x=101.21, default_y=-405.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('17')
                Type('half')
                Stem('down')
                Staff(5)
            with Note(default_x=386.17, default_y=-410.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('17')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(5)
        with Measure(number='5', width=326.96):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Cadential 6-4 chord\n', default_y=42.2, relative_x=-8.68, relative_y=56.49)
                    Words('\n')
                    Words('in e♭ minor \n')
                    Words('\n')
                    Words(None)
                Staff(1)
            with Note(default_x=19.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(4.0)
            with Note(default_x=19.52, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Backup():
                Duration(4.0)
            with Direction(placement='below'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=-54.25, relative_x=-141.53)
                Staff(3)
            with Note(default_x=19.52, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('whole')
                Accidental('flat')
                Notehead('normal', color='#FF00FF')
                Staff(3)
                with Notations():
                    Slur(type='stop', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none', relative_x=-301.3)
                Staff(3)
            with Backup():
                Duration(4.0)
            with Note(default_x=22.48, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('13')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(4)
            with Note(default_x=216.89, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('13')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(4)
                with Notations():
                    Slur(type='stop', number=4)
            with Backup():
                Duration(4.0)
            with Note(default_x=19.52, default_y=-415.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('17')
                Type('whole')
                Accidental('flat')
                Staff(5)
                with Notations():
                    Slur(type='stop', number=5)
            with Barline(location='right'):
                BarStyle('light-heavy')