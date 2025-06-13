with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Aria')
    with Identification():
        Creator('by Unknown BWV 516', type='composer')
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
        CreditWords('Aria', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Warum betrübst du dich', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('by Unknown\n', default_x=1134.19, default_y=1486.67, justify='right', valign='bottom', font_size='12')
        CreditWords('BWV 516\n')
        CreditWords(None)
    with PartList():
        with ScorePart(id='P1'):
            PartName('Stimme')
            PartAbbreviation('St.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Stimme')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Pipe Organ', print_object='no')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Pipe Organ')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(20)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=180.63):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    TopSystemDistance(210.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-4)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=14.7, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('82')
                Sound(tempo=82.0)
            with Note(default_x=132.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='1', width=264.7):
            with Note(default_x=28.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=145.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=197.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=230.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='2', width=146.37):
            with Note(default_x=23.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=103.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='3', width=257.54):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=45.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=74.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=103.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=132.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=161.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=179.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=197.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=226.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='4', width=207.26):
            with Note(default_x=11.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=57.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=102.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        BreathMark(None)
            with Note(default_x=148.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=394.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(145.74)
            with Note(default_x=110.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=184.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=235.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=272.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=295.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=318.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=355.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='6', width=224.7):
            with Note(default_x=25.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=136.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=280.96):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=43.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=77.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=111.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=144.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=212.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=245.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='8', width=156.78):
            with Note(default_x=22.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=162.09):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(145.74)
            with Note(default_x=110.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=261.37):
            with Note(default_x=14.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=76.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=95.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=127.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=189.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=122.04):
            with Note(default_x=19.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=86.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
        with Measure(number='11', width=253.03):
            with Note(default_x=16.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=91.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=119.86, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
            with Note(default_x=145.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.45, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=219.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='12', width=257.96):
            with Note(default_x=22.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=146.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('82')
                Sound(tempo=82.0)
            with Note(default_x=201.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.93, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Offset(-12.0)
                Sound(tempo=76.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.93, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Offset(-10.0)
                Sound(tempo=68.0)
        with Measure(number='13', width=345.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(145.74)
            with Note(default_x=116.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=169.21, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=221.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
            with Note(default_x=307.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='14', width=192.44):
            with Note(default_x=14.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=131.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=326.35):
            with Note(default_x=11.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=49.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=87.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=163.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=286.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='16', width=192.26):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Sound(tempo=76.0)
            with Note(default_x=15.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=13.03, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('58')
                Sound(tempo=58.0)
            with Note(default_x=130.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Offset(-8.0)
                Sound(tempo=68.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='0', implicit='yes', width=180.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(137.42)
            with Attributes():
                Divisions(4.0)
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
            with Note(default_x=132.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wa')
                with Lyric(number='2', default_x=6.58, default_y=-104.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Backup():
                Duration(4.0)
            with Note(default_x=134.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=134.66, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=132.68, default_y=-187.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=155.86, default_y=-182.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='1', width=264.7):
            with Note(default_x=28.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('rum')
                with Lyric(number='2', default_x=9.07, default_y=-104.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('sorgst,')
            with Note(default_x=80.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-104.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('wie')
            with Note(default_x=145.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-78.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('trübst')
                    Extend()
                with Lyric(number='2', default_y=-104.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('will')
                    Extend()
            with Note(default_x=197.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=230.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                with Lyric(number='2', default_x=6.58, default_y=-104.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=82.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=115.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=147.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=147.68, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=232.3, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=232.3, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=30.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=87.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=28.53, default_y=-177.42):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=80.6, default_y=-172.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=145.7, default_y=-192.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=230.33, default_y=-202.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='2', width=146.37):
            with Note(default_x=23.86, default_y=-25.0):
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
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=6.22, default_y=-78.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
                with Lyric(number='2', default_x=6.22, default_y=-104.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('doch')
            with Note(default_x=103.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-104.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('noch')
            with Backup():
                Duration(16.0)
            with Note(default_x=25.94, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=25.94, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=105.89, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=105.89, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.86, default_y=-187.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)
            with Note(default_x=103.91, default_y=-187.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=257.54):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-78.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('beu')
                with Lyric(number='2', default_y=-104.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('end')
            with Note(default_x=45.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=74.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-78.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('gest')
                    Extend()
                with Lyric(number='2', default_y=-104.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
                    Extend()
            with Note(default_x=103.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=132.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-78.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
                    Extend()
                with Lyric(number='2', default_y=-104.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit')
                    Extend()
            with Note(default_x=161.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=179.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=197.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-78.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('zur')
                    Extend()
                with Lyric(number='2', default_y=-104.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
                    Extend()
            with Note(default_x=226.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=20.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=134.52, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=134.52, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=199.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=228.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=21.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.42, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=76.46, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(4.0)
            with Note(default_x=197.87, default_y=-182.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-207.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=45.45, default_y=-202.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=74.48, default_y=-197.42):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=132.55, default_y=-217.42):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=197.87, default_y=-192.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=226.91, default_y=-202.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='4', width=207.26):
            with Note(default_x=11.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_y=-78.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Er')
                with Lyric(number='2', default_y=-104.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wer')
            with Note(default_x=57.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=102.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.84, default_y=-78.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('den,')
                with Lyric(number='2', default_x=8.84, default_y=-104.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('den,')
            with Note(default_x=148.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
                with Lyric(number='2', default_x=6.58, default_y=-104.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=59.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=59.31, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=104.81, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=104.81, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=150.32, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=150.32, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=11.83, default_y=-187.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=57.33, default_y=-202.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=102.84, default_y=-222.42):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-44.6, relative_y=-10.0)
            with Note(default_x=148.35, default_y=-187.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=177.21, default_y=-192.42):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='5', width=394.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(117.22)
            with Note(default_x=110.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-67.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
                with Lyric(number='2', default_x=6.58, default_y=-93.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fäh')
            with Note(default_x=184.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-67.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='2', default_x=6.58, default_y=-93.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('rest')
            with Note(default_x=235.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-67.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('plag')
                with Lyric(number='2', default_y=-93.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ü')
            with Note(default_x=272.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=295.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=318.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-67.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter')
                    Extend()
                with Lyric(number='2', default_y=-93.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('ber')
                    Extend()
            with Note(default_x=355.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=112.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=149.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=186.34, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=186.34, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=237.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=237.21, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=320.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=357.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=117.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(8.0)
            with Note(default_x=325.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=110.38, default_y=-177.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=184.36, default_y=-182.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=235.23, default_y=-187.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=272.22, default_y=-182.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=318.47, default_y=-177.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=224.7):
            with Note(default_x=25.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=5.9, relative_y=10.0)
                with Lyric(number='1', default_x=8.6, default_y=-67.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Geist,')
                with Lyric(number='2', default_x=6.22, default_y=-93.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt')
            with Note(default_x=136.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-67.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
                with Lyric(number='2', default_x=6.58, default_y=-93.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Backup():
                Duration(16.0)
            with Note(default_x=27.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=138.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=181.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=143.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=25.68, default_y=-172.22):
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
                with Notations():
                    Fermata(None, type='inverted', default_y=-42.15, relative_y=-10.0)
            with Note(default_x=136.5, default_y=-182.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='7', width=280.96):
            with Note(default_x=10.0, default_y=-25.0):
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
                with Lyric(number='1', default_y=-67.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ab')
                with Lyric(number='2', default_y=-93.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ü')
            with Note(default_x=43.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=77.34, default_y=-25.0):
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
                with Lyric(number='1', default_y=-67.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge')
                with Lyric(number='2', default_y=-93.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('ber')
                    Extend()
            with Note(default_x=111.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=144.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-67.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mat')
                with Lyric(number='2', default_x=6.58, default_y=-93.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=212.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-67.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter')
                    Extend()
                with Lyric(number='2', default_y=-93.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
                    Extend()
            with Note(default_x=245.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=11.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=79.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=146.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=146.65, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=213.99, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=213.99, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-167.22):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.34, default_y=-177.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=144.68, default_y=-172.22):
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
            with Note(default_x=178.35, default_y=-177.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=212.02, default_y=-172.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=156.78):
            with Note(default_x=22.29, default_y=-25.0):
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
                with Lyric(number='1', default_x=10.99, default_y=-67.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sinn?')
                with Lyric(number='2', default_x=8.11, default_y=-93.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('hin.')
            with Backup():
                Duration(12.0)
            with Note(default_x=24.37, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=24.37, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.29, default_y=-157.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=162.09):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(114.91)
            with Note(default_x=110.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-66.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wirst')
            with Backup():
                Duration(4.0)
            with Note(default_x=112.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=112.35, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=110.38, default_y=-189.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=261.37):
            with Note(default_x=14.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-66.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=56.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='2', default_y=-66.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
                    Extend()
            with Note(default_x=76.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=95.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=127.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-66.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=189.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-66.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('recht')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=58.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=128.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=191.53, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th', size='cue')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=230.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=20.74, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('3')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=133.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('3')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=14.02, default_y=-169.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=56.93, default_y=-169.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=127.14, default_y=-169.91):
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
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=158.35, default_y=-174.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=189.55, default_y=-179.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='10', width=122.04):
            with Note(default_x=19.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=13.4, relative_y=10.0)
                with Lyric(number='2', default_x=6.22, default_y=-66.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('fest')
            with Note(default_x=86.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-66.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Backup():
                Duration(16.0)
            with Note(default_x=21.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=21.34, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=88.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=19.26, default_y=-184.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)
            with Note(default_x=86.27, default_y=-164.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=253.03):
            with Note(default_x=16.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-66.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Got')
            with Note(default_x=59.5, default_y=-5.0):
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
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='2', default_y=-66.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('tes')
                    Extend()
            with Note(default_x=91.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.86, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-66.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wil')
            with Note(default_x=188.45, default_y=-5.0):
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
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='2', default_y=-66.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('len')
                    Extend()
            with Note(default_x=219.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=18.17, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=61.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=147.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=147.12, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=190.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=221.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=59.5, default_y=-144.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(4.0)
            with Note(default_x=195.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=16.2, default_y=-159.91):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=59.5, default_y=-179.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=145.14, default_y=-174.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=188.45, default_y=-169.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=257.96):
            with Note(default_x=22.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.22, default_y=-66.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('grün')
            with Note(default_x=146.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=5.9, relative_y=10.0)
                with Lyric(number='2', default_x=8.84, default_y=-66.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('den,')
            with Note(default_x=201.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-66.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
            with Backup():
                Duration(16.0)
            with Note(default_x=35.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=35.44, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=80.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=148.62, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=148.62, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=203.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=203.48, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=85.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=114.34, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=23.22, default_y=-164.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=78.07, default_y=-199.91):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.65, default_y=-184.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)
            with Note(default_x=201.5, default_y=-149.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=345.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(106.51)
            with Note(default_x=116.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=169.21, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=221.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('E')
            with Note(default_x=307.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('middle')
                    Text('wig')
            with Backup():
                Duration(16.0)
            with Note(default_x=118.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=118.51, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=171.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=171.18, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=223.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=223.85, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=276.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=276.51, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=116.54, default_y=-141.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=169.21, default_y=-146.51):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=221.87, default_y=-151.51):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=274.54, default_y=-156.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=192.44):
            with Note(default_x=14.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=24.65, relative_y=10.0)
                with Lyric(number='2', default_x=6.22, default_y=-78.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('keit')
            with Note(default_x=131.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Backup():
                Duration(16.0)
            with Note(default_x=16.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=16.44, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=133.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=14.36, default_y=-161.51):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-42.15, relative_y=-10.0)
            with Note(default_x=131.16, default_y=-171.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='15', width=326.35):
            with Note(default_x=11.83, default_y=-25.0):
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
                with Lyric(number='2', default_y=-78.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wah')
            with Note(default_x=49.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=87.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='2', default_y=-78.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('re')
                    Extend()
            with Note(default_x=125.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=163.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ru')
            with Note(default_x=286.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.58, default_y=-78.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('he')
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=89.66, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=89.66, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=165.52, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=203.45, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th', size='cue')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=227.16, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=250.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(8.0)
            with Note(default_x=163.04, default_y=-156.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('half', size='cue')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=11.83, default_y=-156.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=87.69, default_y=-171.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=163.55, default_y=-166.51):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=248.89, default_y=-176.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=192.26):
            with Note(default_x=15.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.22, default_y=-78.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fin')
            with Note(default_x=130.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=8.64, default_y=-78.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('den.')
            with Backup():
                Duration(12.0)
            with Note(default_x=17.99, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=100.82, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=132.67, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.38, default_y=-156.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Stem('up')
                Staff(2)
            with Note(default_x=68.96, default_y=-161.51):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=130.7, default_y=-156.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter', size='cue')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.66, default_y=-171.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=130.7, default_y=-191.51):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Fermata(None, type='upright', relative_y=10.0)
                Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)