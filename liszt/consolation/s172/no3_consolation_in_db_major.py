with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Consolation No. 3')
    with Identification():
        Creator('Franz Liszt', type='composer')
        Rights('Public Domain')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(6.96)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1706.9)
            PageWidth(1206.9)
            with PageMargins(type='both'):
                LeftMargin(43.1035)
                RightMargin(43.1035)
                TopMargin(57.4713)
                BottomMargin(57.4713)
        WordFont(font_family='FreeSerif', font_size='12')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Franz Liszt', default_x=1163.79, default_y=1541.43, justify='right', valign='bottom')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Consolations', default_x=603.448, default_y=1649.43, justify='center', valign='top', font_size='25')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('III', default_x=603.448, default_y=1614.27, justify='center', valign='top', font_size='25')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Public Domain', default_x=603.448, default_y=57.4713, justify='center', valign='bottom', font_size='10')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Public Domain', default_x=603.448, default_y=57.4713, justify='center', valign='bottom', font_size='10')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Public Domain', default_x=603.448, default_y=57.4713, justify='center', valign='bottom', font_size='10')
    with Credit(page=4):
        CreditType('rights')
        CreditWords('Public Domain', default_x=603.448, default_y=57.4713, justify='center', valign='bottom', font_size='10')
    with Credit(page=5):
        CreditType('rights')
        CreditWords('Public Domain', default_x=603.448, default_y=57.4713, justify='center', valign='bottom', font_size='10')
    with Credit(page=6):
        CreditType('rights')
        CreditWords('Public Domain', default_x=603.448, default_y=57.4713, justify='center', valign='bottom', font_size='10')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Piano', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=434.73):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(71.87)
                        RightMargin(0.0)
                    TopSystemDistance(151.95)
                with StaffLayout(number=2):
                    StaffDistance(121.65)
            with Attributes():
                Divisions(480.0)
                with Key():
                    Fifths(-5)
                    Mode('major')
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
                    Words('Lento placido', default_x=-44.43, default_y=4.48, relative_x=-38.13, relative_y=20.0, font_weight='bold', font_size='14')
                Staff(1)
                Sound(tempo=65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=7.5, default_y=-40.0, relative_x=-1.51, relative_y=-19.71):
                        Ppp()
                Staff(1)
                Sound(dynamics=17.78)
            with Note():
                Rest(measure='yes')
                Duration(1920.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-84.16)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Direction(placement='above'):
                with DirectionType():
                    Words('sempre legatissimo', default_y=4.81, relative_x=-0.45, relative_y=86.86, font_style='italic')
                Staff(2)
            with Note(default_x=170.67, default_y=-171.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=194.53, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=218.39, default_y=-161.65):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=242.25, default_y=-136.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=266.11, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=289.97, default_y=-161.65):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=313.83, default_y=-171.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=337.69, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=361.55, default_y=-161.65):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=385.41, default_y=-136.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=409.27, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=143.48, default_y=-216.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='2', width=307.04):
            with Note():
                Rest(measure='yes')
                Duration(1920.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=42.98, default_y=-171.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=66.84, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=90.7, default_y=-161.65):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=114.56, default_y=-136.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=138.42, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=162.28, default_y=-161.65):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=186.14, default_y=-171.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.0, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=233.86, default_y=-161.65):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=257.72, default_y=-136.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=281.58, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.8, default_y=-216.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='3', width=307.04):
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('cantando', relative_x=-10.0, relative_y=35.0, font_style='italic')
                Staff(1)
            with Note(default_x=233.86, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=42.98, default_y=-171.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=66.84, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=90.7, default_y=-161.65):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=114.56, default_y=-136.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=138.42, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=162.28, default_y=-161.65):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=186.14, default_y=-171.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.0, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=233.86, default_y=-161.65):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=257.72, default_y=-136.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=281.58, default_y=-146.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.8, default_y=-216.65):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=442.0):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(122.09)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=124.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=276.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=317.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=358.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=399.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-90.91)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=150.66, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=175.86, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=201.05, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=226.25, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=251.44, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=276.64, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=301.83, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=333.33, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=358.52, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=383.72, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=415.21, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=121.18, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='5', width=327.43):
            with Note(default_x=18.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=168.42, default_y=0.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=207.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=247.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=286.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.67)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=47.49, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=71.67, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=95.86, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=120.04, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=144.23, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=168.42, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=192.6, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=222.94, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=247.12, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=271.31, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=301.64, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.8, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='6', width=329.39):
            with Note(default_x=18.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=221.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=241.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.63, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-90.91)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=41.59, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=64.07, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=86.54, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=109.01, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=131.78, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=154.25, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=176.73, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=199.2, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=221.68, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=256.77, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=289.46, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.8, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='7', width=407.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(122.09)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=124.5, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=335.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=147.93, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=171.37, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=194.8, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=218.24, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=241.67, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=265.11, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=288.54, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=311.98, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=335.41, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=358.85, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=382.28, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=121.18, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='8', width=343.27):
            with Note(default_x=18.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=174.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=216.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=257.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=299.79, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-103.25)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=45.29, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=71.06, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=96.83, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=122.6, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.38, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=174.15, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=199.92, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=232.14, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=257.91, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=283.68, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=315.9, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.8, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='9', width=348.23):
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=172.96, default_y=0.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=215.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=257.88, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=304.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=42.33, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=68.45, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=94.58, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=120.71, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=146.84, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.9)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=199.09, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=231.75, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=257.88, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=287.85, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=320.5, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.8, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(960.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=172.6, default_y=-190.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=440.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(122.09)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=120.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=330.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=351.71, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=383.87, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=416.03, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.91)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=144.06, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=167.43, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=190.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=214.16, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=237.53, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=260.89, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=284.26, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=307.63, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=330.99, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=366.88, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=400.87, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=117.38, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1920.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='11', width=308.44):
            with Note(default_x=18.64, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=234.79, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=42.66, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=66.67, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=90.69, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=114.71, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=138.72, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=162.74, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=186.76, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.78, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=234.79, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=258.81, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=282.83, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.32, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1920.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='12', width=349.58):
            with Note(default_x=18.28, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=183.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=224.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=265.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=306.91, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.91)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=43.92, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=73.88, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=107.85, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=133.13, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.41, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=183.68, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=208.96, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=240.56, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=265.83, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=291.11, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=322.7, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.32, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='13', width=467.91):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(122.09)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=121.18, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=287.03, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
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
            with Note(default_x=331.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=376.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=421.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-70.75)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=149.12, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=176.7, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=204.28, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=231.87, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=259.45, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=287.03, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=314.61, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=349.09, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=376.67, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=404.25, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=438.73, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=118.22, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='14', width=257.22):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-61.79)
                Staff(1)
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=44.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.11, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=108.16, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=140.22, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-20.0)
                Staff(1)
            with Note(default_x=172.27, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        StrongAccent(type='up')
            with Note(default_x=223.56, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(1920.0)
            with Note():
                Rest(measure='yes')
                Duration(1920.0)
                Voice('5')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='15', width=373.69):
            with Note(default_x=18.28, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=192.9, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=226.87, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=255.92, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=284.96, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=314.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=343.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(160.0)
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
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-70.75)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=47.68, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=76.73, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=105.77, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=134.81, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.86, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=192.9, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=226.87, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=255.92, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=284.96, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=314.0, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=343.05, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.32, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='16', width=412.69):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=121.18, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
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
            with Note(default_x=145.16, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(160.0)
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
            with Note(default_x=193.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
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
            with Note(default_x=217.09, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=241.06, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(160.0)
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
            with Note(default_x=267.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=291.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=315.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=339.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(160.0)
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
            with Note(default_x=363.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
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
            with Note(default_x=387.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(160.0)
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
                Duration(1920.0)
            with Note():
                Rest(measure='yes')
                Duration(1920.0)
                Voice('5')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=137.93)
                Staff(2)
        with Measure(number='17', width=363.69):
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=180.2, default_y=0.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=226.01, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=271.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=316.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.9)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=40.64, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=68.55, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=96.46, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=124.38, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=152.29, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.9)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=208.57, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=243.46, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=271.37, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=299.29, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=334.18, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=12.36, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=179.84, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=322.44):
            with Note(default_x=19.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-90.91)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=44.26, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.41, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=94.55, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=119.69, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=144.84, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=169.98, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=195.12, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=220.26, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=245.41, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=270.55, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=295.69, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.8, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='19', width=407.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(-0.0)
                    SystemDistance(150.49)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=335.79, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=335.79, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=147.98, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=171.45, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=194.93, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=218.41, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=241.88, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=265.36, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=288.84, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=312.31, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=335.79, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=359.27, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=382.74, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=121.18, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='20', width=350.1):
            with Note(default_x=25.09, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=40.45)
            with Note(default_x=25.09, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.45)
            with Note(default_x=180.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=180.69, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=222.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=222.65, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=264.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=264.6, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=306.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=306.55, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-90.91)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=51.61, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=77.43, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=103.25, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=129.06, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=154.88, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=180.69, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=206.51, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=238.78, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=264.6, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=290.41, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=322.68, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=22.13, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=340.9):
            with Note(default_x=25.09, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=40.45)
            with Note(default_x=25.09, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Arpeggiate(default_x=-13.09, default_y=40.45)
            with Note(default_x=177.94, default_y=0.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=177.94, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=218.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=218.28, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=258.62, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=258.62, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=298.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=298.96, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.67)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=53.81, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=78.64, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=103.46, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=128.29, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=153.11, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=177.94, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=202.76, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=233.79, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=258.62, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=283.44, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=314.48, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=22.13, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='22', width=483.41):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(-0.0)
                    SystemDistance(150.49)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=124.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=124.14, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=264.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=284.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=348.93, default_y=15.0):
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
            with Note(default_x=371.7, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=394.47, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=426.56, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=458.64, default_y=50.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-84.6)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=147.77, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=171.04, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=194.31, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=217.58, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=240.85, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=264.12, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=299.92, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=333.77, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=371.7, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=409.63, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=443.48, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=121.18, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='23', width=287.04):
            with Note(default_x=19.12, default_y=45.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=217.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=217.55, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=41.08, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=63.04, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=84.99, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=106.95, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=129.72, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=151.68, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.63, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.59, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=217.55, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=239.51, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=262.27, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.8, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='24', width=328.37):
            with Note(default_x=18.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=18.76, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=167.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=167.67, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=207.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=207.45, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=247.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=247.22, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=287.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=287.0, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-90.91)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=45.29, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.76, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=94.24, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=118.72, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=143.19, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=167.67, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=192.15, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=222.74, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=247.22, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=271.7, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=302.29, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.8, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='25', width=418.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(150.49)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=121.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=121.18, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-55.46)
                Staff(1)
            with Note(default_x=258.81, default_y=0.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=258.81, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=296.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=296.06, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=333.31, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=333.31, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=378.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=378.44, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=30.0)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=147.7, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=169.79, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=191.88, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=213.96, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=236.73, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.9)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=280.9, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=311.23, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=333.31, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=363.28, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=393.61, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=121.18, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(960.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=258.45, default_y=-190.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=383.82):
            with Note(default_x=18.28, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=18.28, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=161.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=161.05, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=183.81, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.67, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.43, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=71.27)
                Staff(1)
            with Note(default_x=294.2, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.63, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.05, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.79)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=42.38, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=66.11, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=89.84, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=113.58, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.31, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=161.05, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=198.98, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=233.5, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=271.43, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=309.36, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=343.89, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.32, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1920.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='27', width=296.62):
            with Note(default_x=18.64, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1, relative_x=-5.27)
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=225.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=41.66, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.68, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=87.7, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=110.72, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.74, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=156.76, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=179.78, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.8, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=225.82, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=248.84, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=271.86, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.32, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1920.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='28', width=437.51):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(-0.0)
                    SystemDistance(150.49)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=3.3, relative_y=25.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Words('expressivo', default_y=9.81, relative_x=30.0, relative_y=40.0, font_style='italic')
                Staff(1)
            with Note(default_x=120.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=277.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=317.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=356.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=396.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.91)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=145.01, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=174.98, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=199.29, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=229.25, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=253.57, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=277.88, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=302.19, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=332.58, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=356.89, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=381.21, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=411.6, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=117.38, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1920.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='29', width=294.52):
            with Note(default_x=18.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=224.1, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.91)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=41.47, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.3, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=87.13, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=109.96, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=132.78, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=155.61, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=178.44, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=201.27, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=224.1, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=246.93, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=269.76, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.32, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1920.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='30', width=366.79):
            with Note(default_x=51.62, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=211.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=211.3, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=249.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=249.77, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=288.24, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=288.24, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=326.72, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=326.72, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=51.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.45, default_y=0.51, relative_x=-24.53, relative_y=3.31)
            with Note(default_x=51.98, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.45, default_y=0.51, relative_x=-24.53, relative_y=3.31)
            with Backup():
                Duration(240.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.91)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=75.28, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=111.42, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=134.72, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=164.69, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=187.99, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=211.3, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=234.61, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=264.94, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=288.24, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=311.55, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=341.88, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=48.66, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='31', width=438.47):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(100.23)
            with Direction(placement='above'):
                with DirectionType():
                    Words('dolcissimo', default_y=4.7, relative_y=65.0, font_style='italic')
                Staff(1)
            with Note(default_x=129.98, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=129.98, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=280.26, default_y=10.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=280.26, default_y=20.0):
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
            with Note(default_x=321.03, default_y=15.0):
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
            with Note(default_x=321.03, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=359.65, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=359.65, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=398.26, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=398.26, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=156.5, default_y=-140.23):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=179.95, default_y=-115.23):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=203.4, default_y=-130.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=233.37, default_y=-105.23):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=256.81, default_y=-115.23):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=280.26, default_y=-130.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=305.65, default_y=-140.23):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=336.2, default_y=-115.23):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=359.65, default_y=-130.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=383.09, default_y=-105.23):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=413.42, default_y=-115.23):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=127.02, default_y=-185.23):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='32', width=327.55):
            with Note(default_x=17.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=17.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=59.13, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=59.13, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=97.06, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=97.06, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=142.19, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=142.19, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=176.97, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=176.97, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=211.75, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=211.75, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=249.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=249.68, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=287.61, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=287.61, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=43.97, default_y=-140.23):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=74.3, default_y=-115.23):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=97.06, default_y=-130.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=127.03, default_y=-105.23):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=157.36, default_y=-115.23):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=196.59, default_y=-140.23):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=226.92, default_y=-115.23):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=249.68, default_y=-130.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=272.45, default_y=-105.23):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=302.78, default_y=-115.23):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=17.44, default_y=-185.23):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=176.61, default_y=-185.23):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='33', width=332.8):
            with Note(default_x=24.08, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=24.08, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=178.83, default_y=10.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=178.83, default_y=20.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-53.73)
                Staff(1)
            with Note(default_x=217.2, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=217.2, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=254.94, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=254.94, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=292.87, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=292.87, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-14.88)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=50.61, default_y=-140.23):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=80.57, default_y=-120.23):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=103.34, default_y=-130.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=133.3, default_y=-105.23):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=156.07, default_y=-120.23):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=178.83, default_y=-130.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=203.02, default_y=-140.23):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=233.18, default_y=-120.23):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=254.94, default_y=-130.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=277.7, default_y=-105.23):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=308.04, default_y=-120.23):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction():
                with DirectionType():
                    Wedge(type='stop', number=1, relative_y=-35.0)
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=21.12, default_y=-190.23):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Accidental('natural')
                Staff(2)
        with Measure(number='34', width=410.62):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(221.77)
                with StaffLayout(number=2):
                    StaffDistance(186.42)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-53.73)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-210.0)
                Staff(1)
            with Note(default_x=130.34, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=130.34, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2)
                Staff(1)
            with Note(default_x=217.47, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=217.47, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=304.33, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=304.33, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=356.67, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=356.67, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction():
                with DirectionType():
                    Wedge(type='crescendo', number=1, relative_y=-35.0)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=159.74, default_y=-231.42):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=189.7, default_y=-206.42):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=217.47, default_y=-221.42):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=250.66, default_y=-196.42):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=277.5, default_y=-206.42):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(960.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=129.98, default_y=-276.42):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(960.0)
        with Measure(number='35', width=344.0):
            with Note(default_x=20.64, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=20.64, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
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
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=3.3, relative_y=25.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Words('expressivo', default_y=1.43, relative_x=27.02, relative_y=40.0, font_style='italic')
                Staff(1)
            with Note(default_x=271.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Backup():
                Duration(1.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(1.0)
            with Note(default_x=76.09, default_y=-276.42):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.25, default_y=-251.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=128.42, default_y=-266.42):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=152.19, default_y=-241.42):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=175.97, default_y=-251.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=199.75, default_y=-266.42):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=223.52, default_y=-276.42):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=247.3, default_y=-251.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=271.07, default_y=-266.42):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=294.85, default_y=-241.42):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=318.63, default_y=-251.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=17.32, default_y=-261.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Accidental('natural')
                Staff(2)
        with Measure(number='36', width=344.2):
            with Note(default_x=14.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=174.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=216.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=258.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=300.49, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.87)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=40.63, default_y=-271.42):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=70.03, default_y=-256.42):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=96.19, default_y=-266.42):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=122.36, default_y=-246.42):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.27, default_y=-256.42):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=174.18, default_y=-266.42):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=200.09, default_y=-271.42):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=232.48, default_y=-256.42):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=258.39, default_y=-266.42):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=284.3, default_y=-246.42):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=316.69, default_y=-256.42):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='37', width=360.01):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(221.77)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=124.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=283.41, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=139.82, default_y=-180.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=165.98, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=192.15, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=207.36, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=222.57, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=237.78, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=252.99, default_y=-180.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=268.2, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=283.41, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=298.62, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=313.83, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='38', width=353.44):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=29.83, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=201.1, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=201.1, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=231.43, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=231.43, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=261.76, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=261.76, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=292.09, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=292.09, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=30.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=30.19, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(240.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Backup():
                Duration(1.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(1.0)
            with Note(default_x=90.64, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=118.43, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=144.6, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=170.76, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.93, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=201.1, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=216.26, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=246.59, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=261.76, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=276.92, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=307.26, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=26.87, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Accidental('natural')
                Staff(2)
        with Measure(number='39', width=385.37):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=30.19, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=30.19, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=210.36, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=210.36, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=251.96, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=251.96, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=293.56, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=293.56, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=324.02, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=324.02, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('dolcissimo', relative_x=8.12, relative_y=61.5, font_style='italic')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Backup():
                Duration(1.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(1.0)
            with Note(default_x=98.04, default_y=-180.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=124.21, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.37, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=179.77, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.07, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=210.36, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=231.16, default_y=-180.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=272.76, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=293.56, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=308.86, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=339.19, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=27.23, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Accidental('natural')
                Staff(2)
        with Measure(number='40', width=657.15):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(221.77)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=124.02, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=124.02, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=214.11, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=214.11, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=268.45, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=268.45, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=323.41, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=323.41, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=398.68, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=398.68, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=476.73, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=476.73, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=531.06, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=531.06, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=585.4, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=585.4, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Backup():
                Duration(1.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(1.0)
            with Note(default_x=188.55, default_y=-180.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=239.68, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=268.45, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=297.84, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=348.98, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Backup():
                Duration(1.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(1.0)
            with Note(default_x=451.16, default_y=-180.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=502.3, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=531.06, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=559.83, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=610.96, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=123.66, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=398.32, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='41', width=441.67):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=26.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=26.8, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-54.63)
                Staff(1)
            with Note(default_x=151.82, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=151.82, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=151.82, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=245.07, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=245.07, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=245.07, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=346.82, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=346.82, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=346.82, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-6.0)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.9)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Backup():
                Duration(1.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(1.0)
            with Note(default_x=89.65, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.74, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=151.82, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=182.9, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=213.99, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=245.07, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=284.65, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=315.74, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=346.82, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=377.91, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=408.99, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=23.48, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Accidental('flat')
                Staff(2)
        with Measure(number='42', width=1098.82):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    TopSystemDistance(135.03)
                with StaffLayout(number=2):
                    StaffDistance(91.23)
            with Note(default_x=121.18, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=121.18, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=121.18, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('poco rit.', default_y=7.63, relative_y=98.36, font_style='italic')
                Staff(1)
            with Note(default_x=589.87, default_y=15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=589.87, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=589.87, default_y=50.0):
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
            with Note(default_x=716.7, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=716.7, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=716.7, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=843.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=843.54, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=843.54, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=970.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=970.38, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=970.38, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=199.59, default_y=-136.23):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=277.65, default_y=-111.23):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=355.7, default_y=-121.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=433.76, default_y=-96.23):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=511.81, default_y=-111.23):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=589.87, default_y=-121.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=667.92, default_y=-136.23):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=765.49, default_y=-111.23):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=843.54, default_y=-121.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=921.6, default_y=-96.23):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1019.16, default_y=-111.23):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=118.22, default_y=-166.23):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='43', width=374.78):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(250.0)
                with StaffLayout(number=2):
                    StaffDistance(92.4)
            with Note(default_x=124.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=124.14, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=124.14, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-84.16)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=144.5, default_y=-142.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=164.5, default_y=-117.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=184.49, default_y=-132.4):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=204.49, default_y=-97.4):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=227.26, default_y=-117.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=247.26, default_y=-132.4):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=267.26, default_y=-142.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=287.26, default_y=-117.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=307.25, default_y=-132.4):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=327.25, default_y=-97.4):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=350.02, default_y=-117.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=121.18, default_y=-187.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='44', width=269.41):
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=201.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=39.12, default_y=-142.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.12, default_y=-117.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=79.12, default_y=-132.4):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=99.12, default_y=-97.4):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=121.88, default_y=-117.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=141.88, default_y=-132.4):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=161.88, default_y=-142.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.88, default_y=-117.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=201.88, default_y=-132.4):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=221.87, default_y=-97.4):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=244.64, default_y=-117.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.8, default_y=-187.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='45', width=228.11):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=129.39, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=153.67, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=177.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=202.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-84.16)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=30.33, default_y=-152.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.31, default_y=-127.4):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=74.47, default_y=-137.4):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=92.45, default_y=-107.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.41, default_y=-127.4):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(960.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=76.32)
                Staff(2)
        with Measure(number='46', width=226.51):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=134.08, default_y=-35.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=156.64, default_y=-40.0):
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
            with Note(default_x=179.19, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=201.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-84.16)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=29.06, default_y=-152.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=45.75, default_y=-122.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=62.45, default_y=-132.4):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=94.62, default_y=-102.4):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=117.38, default_y=-122.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Note():
                Rest()
                Duration(960.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=75.4)
                Staff(2)
        with Measure(number='47', width=428.1):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=117.5, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.65)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=141.19, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=164.89, default_y=-130.0):
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
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=213.22, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=236.92, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=260.61, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=284.31, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=308.01, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=331.71, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=355.41, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=379.1, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=402.8, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='48', width=303.7):
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=232.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=232.48, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=12.0, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.2, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=58.41, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=83.28, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Backup():
                Duration(1.0)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Forward():
                Duration(1.0)
            with Note(default_x=116.46, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=139.67, default_y=-130.0):
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
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=162.87, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=186.08, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=209.28, default_y=-130.0):
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
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=232.48, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=255.69, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=278.89, default_y=-130.0):
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
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='49', width=367.02):
            with Note(default_x=25.09, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=40.45)
            with Note(default_x=25.09, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.45)
            with Note(default_x=188.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=188.64, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=232.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=232.83, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=277.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=277.03, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=321.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=321.23, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.79)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=52.65, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=79.84, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=107.04, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=134.24, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.44, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=188.64, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=215.83, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=249.83, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=277.03, default_y=-125.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=304.23, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=338.23, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=22.13, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='50', width=406.65):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(171.77)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=124.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=124.14, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=258.82, default_y=0.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=258.82, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=294.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=294.79, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=330.75, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=330.75, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=366.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=366.72, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-84.16)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=152.86, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=173.66, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=194.46, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=215.26, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=238.03, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=258.82, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=279.62, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=309.95, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=330.75, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=351.55, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=381.88, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=121.18, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='51', width=390.34):
            with Note(default_x=18.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=18.76, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=170.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=170.36, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=191.15, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.6, default_y=15.0):
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
            with Note(default_x=278.36, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=301.13, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.35, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=365.57, default_y=50.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-84.16)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=42.57, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=66.03, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=100.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=123.45, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=146.9, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=170.36, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=206.32, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=240.43, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=278.36, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=316.29, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=350.41, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.8, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='52', width=301.83):
            with Note(default_x=15.8, default_y=45.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
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
            with Note(default_x=267.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Tenuto()
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=36.57, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=57.34, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=91.32, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=114.08, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=136.85, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=159.61, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=180.38, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=201.16, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=223.92, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=246.69, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=267.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
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
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='53', width=437.15):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(171.77)
                with StaffLayout(number=2):
                    StaffDistance(232.43)
            with Note(default_x=124.14, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=238.42, default_y=-45.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=255.25, default_y=-20.0):
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
            with Note(default_x=285.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=315.92, default_y=-5.0):
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
            with Note(default_x=332.75, default_y=-10.0):
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
            with Note(default_x=351.72, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=382.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=412.38, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-84.16)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=143.48, default_y=-292.43):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=162.47, default_y=-267.43):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=181.46, default_y=-277.43):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=200.44, default_y=-242.43):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.43, default_y=-267.43):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=238.42, default_y=-277.43):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=270.42, default_y=-292.43):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=300.75, default_y=-267.43):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=332.75, default_y=-277.43):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=366.88, default_y=-242.43):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=397.22, default_y=-267.43):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=121.18, default_y=-327.43):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='54', width=252.62):
            with Note(default_x=15.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=212.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=33.63, default_y=-292.43):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.46, default_y=-267.43):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=69.3, default_y=-277.43):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=88.26, default_y=-242.43):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=107.23, default_y=-267.43):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=125.06, default_y=-277.43):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=142.89, default_y=-292.43):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.73, default_y=-267.43):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=178.56, default_y=-277.43):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=197.52, default_y=-242.43):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=227.85, default_y=-267.43):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='55', width=409.05):
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-210.0)
                Staff(1)
            with Note(default_x=85.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=295.26, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=323.62, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=353.96, default_y=-10.0):
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
            with Note(default_x=384.29, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=85.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-44.73, default_y=-14.55, relative_x=-37.37, relative_y=-11.2)
            with Note(default_x=85.1, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(4)
                Duration(1440.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-44.73, default_y=-14.55, relative_x=-37.37, relative_y=-11.2)
            with Forward():
                Duration(240.0)
            with Note(default_x=353.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1800.0)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.36, default_y=-292.43):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=140.17, default_y=-267.43):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=168.53, default_y=-282.43):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=200.7, default_y=-247.43):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.66, default_y=-267.43):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=238.56, default_y=-282.43):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=257.46, default_y=-292.43):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=276.36, default_y=-267.43):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=295.26, default_y=-282.43):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=338.79, default_y=-247.43):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=369.12, default_y=-267.43):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=82.14, default_y=-327.43):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='56', width=1098.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(171.77)
                with StaffLayout(number=2):
                    StaffDistance(204.2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('smor   -    -    -    -    -    -    -    -    -   zan    -    -    -    -    -     -     -     -    -   do', default_y=-195.96, relative_x=-5.0, relative_y=-25.0, font_style='italic', font_size='11')
                Staff(1)
            with Note(default_x=123.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=154.03, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.01, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=245.5, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=275.98, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=306.47, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.96, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=65.0)
                Staff(1)
            with Note(default_x=367.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=397.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=428.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=458.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=489.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=519.9, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=550.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=580.88, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=611.37, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=641.86, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=672.34, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=702.83, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=733.32, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=763.81, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=794.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=824.79, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=855.28, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=885.77, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=916.26, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=946.75, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=977.24, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=1007.73, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=1038.22, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=1068.7, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('16th', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Backup():
                Duration(3840.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=184.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=306.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=428.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=550.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=672.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=794.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=916.26, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=1038.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
        with Measure(number='57', width=1098.82):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    TopSystemDistance(85.18)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Ppp()
                Staff(1)
                Sound(dynamics=17.78)
            with Note(default_x=140.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=140.98, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=600.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=600.16, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
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
            with Note(default_x=724.43, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=724.43, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=848.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=848.69, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=972.95, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=972.95, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=141.34, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(7)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=141.34, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-84.16)
                Staff(2)
            with Note():
                Rest()
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=217.81, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=294.28, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=370.75, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=447.22, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=523.69, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=600.16, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=676.63, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=772.22, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=848.69, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=925.16, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1020.75, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=138.02, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1920.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='58', width=473.71):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.87)
                        RightMargin(0.0)
                    SystemDistance(250.0)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=121.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=121.18, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=165.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.05, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=208.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=208.91, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=252.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=252.78, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=296.65, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=296.65, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=340.51, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=340.51, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=384.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=384.38, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=428.25, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=428.25, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=148.17, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=181.92, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=208.91, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=235.91, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=269.65, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=323.64, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=357.39, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=384.38, default_y=-130.0):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=411.38, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=445.12, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
        with Measure(number='59', width=254.61):
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=45.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=45.45, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=75.1, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=75.1, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('rit.', default_y=-40.0, relative_y=-40.0, font_style='italic')
                Staff(1)
            with Note(default_x=104.75, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=104.75, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=134.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=134.41, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=164.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.06, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=193.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=193.71, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('per   -    -    -  den   -     -     -     -  dosi.', default_y=-40.6, relative_y=-40.0, font_style='italic')
                Staff(1)
            with Note(default_x=223.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=223.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest(measure='yes')
                Duration(1920.0)
                Voice('5')
                Staff(2)
        with Measure(number='60', width=186.35):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
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
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=55.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=55.19, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=98.37, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=98.37, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=141.56, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=141.56, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(1920.0)
            with Note():
                Rest(measure='yes')
                Duration(1920.0)
                Voice('5')
                Staff(2)
        with Measure(number='61', width=184.14):
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=85.09, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=85.09, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest(measure='yes')
                Duration(1920.0)
                Voice('5')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=150.0)
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')