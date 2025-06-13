with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Étude Op. 10 No. 10 in A♭ major')
    with Identification():
        Creator('Frédéric Chopin', type='composer')
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
            PageHeight(2381.64)
            PageWidth(1683.28)
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
        CreditWords('Étude Op. 10 No. 10 in A♭ major', default_x=841.641, default_y=2324.95, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Frédéric Chopin', default_x=1626.59, default_y=2224.95, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('鋼琴')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('鋼琴')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=189.24):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(179.2)
                with StaffLayout(number=2):
                    StaffDistance(98.46)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-4)
                with Time():
                    Beats('12')
                    BeatType('8')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Assai vivace', default_x=-47.49, relative_y=50.0, font_weight='bold', font_size='13')
                Staff(1)
                Sound(tempo=228.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='yes', default_x=-47.49, relative_x=145.0, relative_y=50.0):
                        BeatUnit('quarter')
                        BeatUnitDot()
                        PerMinute('152')
                Staff(1)
                Sound(tempo=228.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-47.49, default_y=-83.8, relative_y=-30.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=142.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
            with Backup():
                Duration(1.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='1', width=525.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=-53.2, relative_y=-30.0):
                        BeatUnit('quarter')
                        PerMinute('268')
                Staff(1)
                Sound(tempo=268.0)
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=52.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.86, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=95.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=138.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=138.59, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=181.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=224.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=224.31, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=267.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=310.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=310.04, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=352.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=395.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=395.76, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=438.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=481.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=481.48, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-173.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=52.86, default_y=-128.46):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.72, default_y=-138.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=138.59, default_y=-153.46, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.45, default_y=-118.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=224.31, default_y=-138.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=3)
            with Note(default_x=267.17, default_y=-173.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=310.04, default_y=-128.46):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=352.9, default_y=-138.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=395.76, default_y=-153.46, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=438.62, default_y=-118.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=481.48, default_y=-138.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Forward():
                Duration(3.0)
            with Note(default_x=138.23, default_y=-153.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(2.0)
            with Note(default_x=395.4, default_y=-153.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Dot()
                Stem('up')
                Notehead('normal', filled='no')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=423.18):
            with Note(default_x=16.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=49.98, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=49.98, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=83.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=117.55, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=117.55, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=151.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=185.11, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=185.11, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=218.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=252.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=252.67, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=286.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=320.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=320.24, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=354.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=387.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=387.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=16.2, default_y=-173.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=49.98, default_y=-123.46):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.76, default_y=-143.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=117.55, default_y=-153.46, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.33, default_y=-118.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.11, default_y=-143.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=218.89, default_y=-173.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=252.67, default_y=-128.46):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=286.45, default_y=-138.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=320.24, default_y=-153.46, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=354.02, default_y=-118.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=387.8, default_y=-138.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.2, default_y=-153.46, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Forward():
                Duration(1.0)
            with Note(default_x=117.18, default_y=-153.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(2.0)
            with Note(default_x=319.87, default_y=-153.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Dot()
                Stem('up')
                Notehead('normal', filled='no')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='3', width=410.54):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-87.26)
                Staff(1)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=43.25, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=76.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=109.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=109.74, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=142.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=176.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=176.23, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=209.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=242.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=242.72, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=275.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=309.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=309.21, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=342.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=375.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=375.7, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-173.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=43.25, default_y=-123.46):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=76.49, default_y=-143.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=109.74, default_y=-153.46, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=142.98, default_y=-118.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=176.23, default_y=-143.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=209.47, default_y=-173.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=242.72, default_y=-128.46):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=275.96, default_y=-138.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=309.21, default_y=-153.46, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=342.45, default_y=-118.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=375.7, default_y=-138.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-153.46, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Forward():
                Duration(1.0)
            with Note(default_x=109.37, default_y=-153.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(2.0)
            with Note(default_x=309.21, default_y=-153.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(1.0)
        with Measure(number='4', width=594.23):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(171.07)
                with StaffLayout(number=2):
                    StaffDistance(105.22)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-41.2, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=110.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=150.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.57, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=190.75, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=230.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=230.94, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=271.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=311.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=311.32, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=351.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=391.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=391.69, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=431.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=472.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=472.07, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=512.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=552.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=552.45, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=110.38, default_y=-175.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=150.57, default_y=-130.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=190.75, default_y=-140.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=230.94, default_y=-145.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=271.13, default_y=-130.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=311.32, default_y=-140.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=351.51, default_y=-195.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=391.69, default_y=-130.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=431.88, default_y=-140.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=472.07, default_y=-160.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=512.26, default_y=-130.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=552.45, default_y=-140.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Forward():
                Duration(3.0)
            with Note(default_x=230.94, default_y=-145.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(4.0)
            with Note(default_x=472.07, default_y=-160.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(1.0)
        with Measure(number='5', width=531.94):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-83.58)
                Staff(1)
            with Note(default_x=53.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.36, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=96.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=140.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=140.08, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=183.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=226.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=226.81, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=270.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=313.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=313.53, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=356.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=400.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=400.25, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=443.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=486.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=486.98, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=10.0, default_y=-180.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=53.36, default_y=-135.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.72, default_y=-145.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=140.08, default_y=-160.22, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.45, default_y=-125.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=226.81, default_y=-145.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=270.17, default_y=-180.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=313.53, default_y=-135.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=356.89, default_y=-145.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=400.25, default_y=-160.22, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=443.62, default_y=-125.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=486.98, default_y=-145.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Forward():
                Duration(3.0)
            with Note(default_x=139.72, default_y=-160.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(2.0)
            with Note(default_x=399.89, default_y=-160.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Dot()
                Stem('up')
                Notehead('normal', filled='no')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='6', width=422.73):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-48.58, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=16.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=49.94, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=49.94, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=83.69, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=117.43, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=117.43, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=151.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=184.92, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=184.92, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-81.13)
                Staff(1)
            with Note(default_x=218.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=252.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=252.41, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=286.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=319.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=319.9, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=353.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=387.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=387.39, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=16.2, default_y=-180.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=49.94, default_y=-130.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.69, default_y=-150.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=117.43, default_y=-160.22, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.18, default_y=-125.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.92, default_y=-150.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=218.67, default_y=-180.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=252.41, default_y=-135.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=286.16, default_y=-145.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=319.9, default_y=-160.22, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=353.64, default_y=-125.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=387.39, default_y=-145.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.2, default_y=-160.22, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Forward():
                Duration(1.0)
            with Note(default_x=117.07, default_y=-160.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(2.0)
            with Note(default_x=319.9, default_y=-160.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(1.0)
        with Measure(number='7', width=570.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(192.47)
                with StaffLayout(number=2):
                    StaffDistance(108.32)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=110.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=146.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=146.81, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-92.26)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-92.26)
                Staff(1)
            with Note(default_x=183.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=219.68, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=219.68, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=256.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=292.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=292.55, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=328.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=380.3, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=380.3, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=416.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=453.17, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=453.17, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=489.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=532.1, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=532.1, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=110.38, default_y=-178.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=146.81, default_y=-133.32):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.24, default_y=-143.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.68, default_y=-148.32):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=256.11, default_y=-133.32):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=292.55, default_y=-143.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=328.98, default_y=-163.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=380.3, default_y=-178.32):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=416.74, default_y=-188.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=453.17, default_y=-198.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=489.6, default_y=-173.32):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=532.1, default_y=-188.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Forward():
                Duration(3.0)
            with Note(default_x=219.68, default_y=-148.32):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(4.0)
            with Note(default_x=453.17, default_y=-198.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(1.0)
        with Measure(number='8', width=529.46):
            with Note(default_x=13.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=55.75, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=55.75, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=72.76, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('258')
                Staff(1)
                Sound(tempo=258.0)
            with Note(default_x=97.71, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=139.66, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=139.66, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=72.37, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('248')
                Staff(1)
                Sound(tempo=248.0)
            with Note(default_x=181.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=223.56, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=223.56, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-52.26, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=68.44, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('238')
                Staff(1)
                Sound(tempo=238.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-92.26)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-92.26)
                Staff(1)
            with Note(default_x=276.15, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('dolce', default_y=1.79, relative_x=-30.0, relative_y=45.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=318.1, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=318.1, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=63.74, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('228')
                Staff(1)
                Sound(tempo=228.0)
            with Note(default_x=360.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=402.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=402.0, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=48.86, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('218')
                Staff(1)
                Sound(tempo=218.0)
            with Note(default_x=443.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=485.91, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=485.91, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-203.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=55.75, default_y=-168.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.71, default_y=-188.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=139.66, default_y=-203.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.61, default_y=-173.32):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=223.56, default_y=-193.32):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=276.15, default_y=-163.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=318.1, default_y=-118.32):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=360.05, default_y=-128.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=402.0, default_y=-133.32, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=443.96, default_y=-118.32):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=485.91, default_y=-128.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-203.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(1.0)
            with Note(default_x=139.66, default_y=-203.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(4.0)
            with Note(default_x=402.0, default_y=-133.32):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='9', width=449.31):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-52.26, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=34.7, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('268')
                Staff(1)
                Sound(tempo=268.0)
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=45.93, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=81.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=3)
            with Note(default_x=117.78, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=153.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=189.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=4)
            with Note(default_x=189.64, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=225.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=261.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=5)
            with Note(default_x=261.5, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=297.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=339.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=6)
            with Note(default_x=339.92, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=375.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=411.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=411.78, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=81.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=153.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=4)
            with Note(default_x=225.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=5)
            with Note(default_x=297.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=6)
            with Note(default_x=375.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-183.32):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=45.93, default_y=-138.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.86, default_y=-148.32):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=117.78, default_y=-163.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=153.71, default_y=-128.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=189.64, default_y=-148.32):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=225.57, default_y=-183.32):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=261.5, default_y=-138.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=297.43, default_y=-148.32):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=339.92, default_y=-163.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=375.85, default_y=-128.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=411.78, default_y=-148.32):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='10', width=581.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(173.52)
                with StaffLayout(number=2):
                    StaffDistance(102.14)
            with Note(default_x=121.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.74, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=3)
            with Note(default_x=159.74, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=197.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=236.06, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=4)
            with Note(default_x=236.06, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=274.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=312.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=5)
            with Note(default_x=312.37, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=350.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=388.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=6)
            with Note(default_x=388.69, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-84.81)
                Staff(1)
            with Note(default_x=426.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=465.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=465.0, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=503.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=541.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=541.31, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
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
            with Note(default_x=121.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=197.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=4)
            with Note(default_x=274.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=5)
            with Note(default_x=350.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=6)
            with Note(default_x=426.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=503.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=4)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=121.58, default_y=-177.14):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=159.74, default_y=-127.14):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=197.9, default_y=-147.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=236.06, default_y=-157.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.21, default_y=-122.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=312.37, default_y=-147.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=350.53, default_y=-177.14):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=388.69, default_y=-132.14):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=426.84, default_y=-142.14):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=465.0, default_y=-157.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=503.16, default_y=-122.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=541.31, default_y=-142.14):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='11', width=449.73):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-49.81, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=46.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=5)
            with Note(default_x=46.51, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=83.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=119.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=6)
            with Note(default_x=119.53, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=156.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=192.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=192.55, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=229.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=265.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=265.57, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=302.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=338.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=338.6, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=375.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=411.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=411.62, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=5)
            with Note(default_x=83.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=6)
            with Note(default_x=156.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=5)
            with Note(default_x=229.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=6)
            with Note(default_x=302.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=375.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-177.14):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=46.51, default_y=-127.14):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.02, default_y=-147.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=119.53, default_y=-157.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=156.04, default_y=-122.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=192.55, default_y=-147.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=229.06, default_y=-177.14):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=265.57, default_y=-132.14):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=302.08, default_y=-142.14):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=338.6, default_y=-157.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=375.11, default_y=-122.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=411.62, default_y=-142.14):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='12', width=518.11):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=52.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=52.21, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=94.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=136.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=136.63, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=178.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=221.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=221.04, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=263.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=305.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=305.46, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-86.19)
                Staff(1)
            with Note(default_x=347.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=389.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=389.88, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=432.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=474.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=1)
            with Note(default_x=474.3, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
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
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=94.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=178.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=263.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=347.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=432.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.01)
                Staff(2)
            with Note(default_x=10.0, default_y=-172.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=52.21, default_y=-127.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.42, default_y=-137.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=136.63, default_y=-142.14):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=178.84, default_y=-127.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=221.04, default_y=-137.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=263.25, default_y=-192.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=305.46, default_y=-127.14):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=347.67, default_y=-137.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=389.88, default_y=-157.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=432.09, default_y=-127.14):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=474.3, default_y=-137.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='13', width=623.52):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(166.16)
                with StaffLayout(number=2):
                    StaffDistance(107.64)
            with Direction(placement='below'):
                with DirectionType():
                    Words('staccato', default_y=-40.0, relative_y=-55.0, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=110.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=153.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=153.01, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=195.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=238.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=238.26, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=280.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=323.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=323.52, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=366.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-89.71)
                Staff(1)
            with Note(default_x=408.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=408.77, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=451.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=494.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=494.03, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=536.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=579.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=579.29, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=110.38, default_y=-182.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=153.01, default_y=-137.64):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=195.63, default_y=-147.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=238.26, default_y=-162.64):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=280.89, default_y=-127.64):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=323.52, default_y=-147.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=366.15, default_y=-182.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=408.77, default_y=-137.64):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=451.4, default_y=-147.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=494.03, default_y=-162.64):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=536.66, default_y=-127.64):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=579.29, default_y=-147.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='14', width=420.27):
            with Note(default_x=16.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=49.74, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=49.74, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-54.71, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=83.28, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=116.82, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=116.82, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=150.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=183.9, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=183.9, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=217.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=250.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=250.98, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=284.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-89.81)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-89.81)
                Staff(1)
            with Note(default_x=318.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=318.06, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=351.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=385.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=385.13, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.2, default_y=-182.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=49.74, default_y=-132.64):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=83.28, default_y=-152.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=116.82, default_y=-162.64):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=150.36, default_y=-127.64):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=183.9, default_y=-152.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=217.44, default_y=-182.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=250.98, default_y=-137.64):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=284.52, default_y=-147.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=318.06, default_y=-152.64):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=351.6, default_y=-127.64):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=385.13, default_y=-147.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='15', width=505.12):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=51.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=51.13, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=92.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=133.38, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=133.38, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=174.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=215.63, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=215.63, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=32.62)
                Staff(1)
            with Note(default_x=256.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=297.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=297.88, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=339.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=380.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=380.14, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=421.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=462.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=462.39, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-167.64):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=51.13, default_y=-122.64):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.25, default_y=-132.64):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=133.38, default_y=-147.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=174.51, default_y=-122.64):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=215.63, default_y=-132.64):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=256.76, default_y=-167.64):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=297.88, default_y=-122.64):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=339.01, default_y=-132.64):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=380.14, default_y=-147.64):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=421.26, default_y=-122.64):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=462.39, default_y=-132.64):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='16', width=576.67):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(168.62)
                with StaffLayout(number=2):
                    StaffDistance(112.49)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=34.91, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('258')
                Staff(1)
                Sound(tempo=258.0)
            with Note(default_x=110.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=148.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=148.64, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=27.41, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('238')
                Staff(1)
                Sound(tempo=238.0)
            with Note(default_x=186.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=225.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=225.15, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=27.41, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('218')
                Staff(1)
                Sound(tempo=218.0)
            with Note(default_x=263.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=301.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=301.67, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=27.41, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('208')
                Staff(1)
                Sound(tempo=208.0)
            with Note(default_x=339.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=378.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=378.18, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=19.56, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('198')
                Staff(1)
                Sound(tempo=198.0)
            with Note(default_x=416.44, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=454.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=454.7, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.77, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('188')
                Staff(1)
                Sound(tempo=188.0)
            with Note(default_x=492.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=10.86, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('40')
                Staff(1)
                Sound(tempo=40.0)
            with Note(default_x=531.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=531.21, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=110.38, default_y=-167.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=148.64, default_y=-122.49):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=186.89, default_y=-132.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=225.15, default_y=-137.49):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=263.41, default_y=-122.49):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=301.67, default_y=-132.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=339.92, default_y=-187.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=378.18, default_y=-142.49):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=416.44, default_y=-152.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=454.7, default_y=-167.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=492.95, default_y=-132.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=531.21, default_y=-152.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='17', width=518.54):
            with Attributes():
                with Key():
                    Fifths(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-70.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=26.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('268')
                Staff(1)
                Sound(tempo=268.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('legatissimo', default_y=56.0, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=98.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=133.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=133.49, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=168.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=203.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=203.21, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=238.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=272.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=272.93, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=307.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=342.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=342.65, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=377.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=412.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=412.37, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=447.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=482.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=482.08, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=98.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=168.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=238.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=307.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=377.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=447.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=98.63, default_y=-202.49):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=133.49, default_y=-147.49):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.35, default_y=-167.49):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.21, default_y=-182.49):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=238.07, default_y=-147.49):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=272.93, default_y=-167.49):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=307.79, default_y=-202.49):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=342.65, default_y=-152.49):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=377.51, default_y=-162.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=412.37, default_y=-177.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=447.22, default_y=-152.49):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=482.08, default_y=-162.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='18', width=453.69):
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=50.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=50.32, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=86.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=123.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=123.37, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=159.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=196.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=196.42, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=232.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=269.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=269.47, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=305.99, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=342.52, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=342.52, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=379.04, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=415.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=415.57, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=13.8, default_y=-202.49):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.32, default_y=-152.49):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=86.85, default_y=-172.49):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=123.37, default_y=-182.49):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=159.9, default_y=-147.49):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.42, default_y=-172.49):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=232.95, default_y=-202.49):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=269.47, default_y=-157.49):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=305.99, default_y=-167.49):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=342.52, default_y=-182.49):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=379.04, default_y=-147.49):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=415.57, default_y=-167.49):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='19', width=567.83):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(88.29)
            with Note(default_x=115.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=152.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=152.61, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=190.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=227.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=227.82, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=265.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=303.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=303.02, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=340.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=378.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=378.22, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=415.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=453.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=453.43, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=491.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=528.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=528.63, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=115.01, default_y=-178.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=152.61, default_y=-128.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=190.22, default_y=-138.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=227.82, default_y=-158.29):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=265.42, default_y=-123.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=303.02, default_y=-138.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=340.62, default_y=-178.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=378.22, default_y=-128.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=415.82, default_y=-148.29):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=453.43, default_y=-158.29):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=491.03, default_y=-123.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=528.63, default_y=-148.29):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='20', width=466.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-41.94, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=51.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.4, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=89.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=126.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=126.6, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=164.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=201.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=201.81, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=239.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=277.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=277.01, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=314.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=352.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=352.21, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=389.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=427.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=427.42, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=13.8, default_y=-178.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=51.4, default_y=-128.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.0, default_y=-138.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=126.6, default_y=-158.29):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=164.21, default_y=-123.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=201.81, default_y=-138.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=239.41, default_y=-178.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=277.01, default_y=-128.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=314.61, default_y=-148.29):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=352.21, default_y=-158.29):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=389.81, default_y=-123.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=427.42, default_y=-138.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='21', width=514.46):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=55.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=55.39, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=96.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=138.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=138.56, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=180.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=221.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=221.74, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=263.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=304.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=304.92, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=346.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=388.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=388.09, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=429.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=471.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=471.27, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=13.8, default_y=-178.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=55.39, default_y=-123.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.98, default_y=-143.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=138.56, default_y=-158.29):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=180.15, default_y=-123.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=221.74, default_y=-143.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.01)
                Staff(2)
            with Note(default_x=263.33, default_y=-178.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=304.92, default_y=-128.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=346.51, default_y=-143.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=388.09, default_y=-153.29):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=429.68, default_y=-128.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=471.27, default_y=-143.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='22', width=491.02):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(156.66)
                with StaffLayout(number=2):
                    StaffDistance(73.97)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('258')
                Staff(1)
                Sound(tempo=258.0)
            with Note(default_x=115.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=145.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.75, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=2.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('238')
                Staff(1)
                Sound(tempo=238.0)
            with Note(default_x=176.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=207.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=207.21, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=5.11, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('218')
                Staff(1)
                Sound(tempo=218.0)
            with Note(default_x=237.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=268.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=268.68, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.93, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('208')
                Staff(1)
                Sound(tempo=208.0)
            with Note(default_x=299.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=330.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=330.15, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.93, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('198')
                Staff(1)
                Sound(tempo=198.0)
            with Note(default_x=360.88, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=391.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=391.62, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.93, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('188')
                Staff(1)
                Sound(tempo=188.0)
            with Note(default_x=422.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=453.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=453.09, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=115.01, default_y=-163.97):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=145.75, default_y=-113.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=176.48, default_y=-133.97):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.21, default_y=-143.97):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=237.95, default_y=-108.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=268.68, default_y=-133.97):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=299.42, default_y=-163.97):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=330.15, default_y=-118.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=360.88, default_y=-128.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=391.62, default_y=-143.97):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=422.35, default_y=-108.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=453.09, default_y=-128.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='23', width=527.11):
            with Attributes():
                with Key():
                    Fifths(-4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.9, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('268')
                Staff(1)
                Sound(tempo=268.0)
            with Note(default_x=97.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=132.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=132.98, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=168.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=203.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=203.75, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=239.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=277.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=277.83, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-76.25)
                Staff(1)
            with Note(default_x=313.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=348.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=348.59, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=383.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=419.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=419.36, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=454.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=490.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=490.13, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=97.6, default_y=-163.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.98, default_y=-98.97):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.37, default_y=-118.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.75, default_y=-128.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=239.13, default_y=-93.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=277.83, default_y=-118.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=313.21, default_y=-163.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=348.59, default_y=-98.97):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=383.98, default_y=-118.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=419.36, default_y=-128.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=454.74, default_y=-93.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=490.13, default_y=-118.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='24', width=530.78):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=53.26, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=53.26, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=96.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=139.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=139.79, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=183.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=226.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=226.32, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=269.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=312.85, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=312.85, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=356.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=399.38, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=399.38, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=442.65, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=485.91, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=485.91, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=10.0, default_y=-148.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=53.26, default_y=-103.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.53, default_y=-113.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=139.79, default_y=-118.97):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.06, default_y=-93.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=226.32, default_y=-113.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=269.59, default_y=-148.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=312.85, default_y=-103.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=356.12, default_y=-113.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=399.38, default_y=-118.97):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=442.65, default_y=-93.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=485.91, default_y=-113.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='25', width=622.41):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(145.3)
                with StaffLayout(number=2):
                    StaffDistance(77.72)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=121.58, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=163.19, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=163.19, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=204.79, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=246.39, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=246.39, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=287.99, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=329.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=329.59, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Fp()
                Staff(1)
                Sound(dynamics=66.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=371.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=412.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=412.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=454.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=496.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=496.0, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=537.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=579.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=579.21, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=121.58, default_y=-172.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=163.19, default_y=-92.72):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=204.79, default_y=-102.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=246.39, default_y=-117.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=287.99, default_y=-92.72):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=329.59, default_y=-102.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=371.2, default_y=-157.72):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=412.8, default_y=-102.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=454.4, default_y=-112.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=496.0, default_y=-127.72):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=537.61, default_y=-102.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=579.21, default_y=-112.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='26', width=522.11):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=52.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=52.54, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=95.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=137.63, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
            with Note(default_x=180.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=222.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=222.71, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-86.19)
                Staff(1)
            with Note(default_x=265.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=307.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=307.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=350.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=392.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=392.88, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=435.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=477.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=477.97, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-152.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=52.54, default_y=-102.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.09, default_y=-117.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.63, default_y=-127.72):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=180.17, default_y=-102.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=222.71, default_y=-117.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=265.26, default_y=-152.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=307.8, default_y=-107.72):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=350.34, default_y=-117.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=392.88, default_y=-122.72):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=435.43, default_y=-107.72):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=477.97, default_y=-117.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='27', width=404.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('sotto voce', default_y=5.52, relative_y=20.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=13.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=46.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=46.22, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=78.63, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=111.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=111.05, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=143.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=175.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=175.88, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dimin.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-91.31)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-91.31)
                Staff(1)
            with Note(default_x=208.29, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=240.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=240.71, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=273.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=305.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=305.54, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=337.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=370.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=370.37, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=13.8, default_y=-172.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=46.22, default_y=-117.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=78.63, default_y=-137.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.05, default_y=-152.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=143.46, default_y=-117.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=175.88, default_y=-137.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=208.29, default_y=-172.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=240.71, default_y=-117.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=273.12, default_y=-137.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=305.54, default_y=-152.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=337.95, default_y=-117.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=370.37, default_y=-137.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='28', width=557.21):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(152.37)
                with StaffLayout(number=2):
                    StaffDistance(83.39)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.89, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('258')
                Staff(1)
                Sound(tempo=258.0)
            with Note(default_x=114.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('poco rit.', default_y=-44.79, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=150.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=150.5, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=63.33)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.89, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('238')
                Staff(1)
                Sound(tempo=238.0)
            with Note(default_x=186.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=223.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=223.14, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.89, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('218')
                Staff(1)
                Sound(tempo=218.0)
            with Note(default_x=259.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=295.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=295.77, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=35.56, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('208')
                Staff(1)
                Sound(tempo=208.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-78.7)
                Staff(1)
            with Note(default_x=332.09, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=368.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=368.41, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=37.58, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('198')
                Staff(1)
                Sound(tempo=198.0)
            with Note(default_x=404.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=441.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=441.05, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=35.32, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('188')
                Staff(1)
                Sound(tempo=188.0)
            with Note(default_x=477.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=45.36)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=25.96, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=513.69, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=513.69, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=114.18, default_y=-178.39):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=150.5, default_y=-123.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.82, default_y=-143.39):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=223.14, default_y=-158.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=259.46, default_y=-123.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=295.77, default_y=-143.39):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=332.09, default_y=-178.39):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=368.41, default_y=-123.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=404.73, default_y=-143.39):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=441.05, default_y=-158.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=477.37, default_y=-123.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=513.69, default_y=-143.39):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='29', width=549.98):
            with Attributes():
                with Key():
                    Fifths(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', default_y=16.02, relative_y=20.0, font_weight='bold', font_style='italic', font_size='13')
                Staff(1)
                Sound(tempo=268.0)
            with Note(default_x=94.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=132.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=132.63, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=170.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=208.22, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=208.22, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=246.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=283.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=283.81, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=321.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=359.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=359.4, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=397.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=435.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=435.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=472.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=510.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=510.59, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=94.83, default_y=-158.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.63, default_y=-103.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=170.42, default_y=-123.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=208.22, default_y=-138.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=246.02, default_y=-103.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=283.81, default_y=-123.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=321.61, default_y=-158.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=359.4, default_y=-108.39):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=397.2, default_y=-123.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=435.0, default_y=-133.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=472.79, default_y=-108.39):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=510.59, default_y=-123.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='30', width=441.71):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=45.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=45.84, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=81.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=117.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.53, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=153.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=189.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=189.21, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=225.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=260.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=260.9, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=296.74, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=332.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=332.58, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=368.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=404.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=404.27, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-158.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=45.84, default_y=-108.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.69, default_y=-128.39):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=117.53, default_y=-138.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=153.37, default_y=-103.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=189.21, default_y=-128.39):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=225.06, default_y=-158.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=260.9, default_y=-113.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=296.74, default_y=-123.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=332.58, default_y=-138.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=368.43, default_y=-103.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=404.27, default_y=-123.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='31', width=559.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(96.01)
            with Note(default_x=111.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=148.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.44, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=185.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=222.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=222.88, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=260.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=297.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=297.33, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=334.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=371.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=371.78, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=409.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=446.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=446.23, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=483.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=520.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=520.67, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=111.21, default_y=-171.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=148.44, default_y=-121.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.66, default_y=-131.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=222.88, default_y=-151.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=260.11, default_y=-116.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=297.33, default_y=-131.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=334.55, default_y=-171.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=371.78, default_y=-121.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=409.0, default_y=-141.01):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=446.23, default_y=-151.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=483.45, default_y=-116.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=520.67, default_y=-141.01):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='32', width=487.4):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=49.65, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=49.65, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=89.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=128.95, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=128.95, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=168.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=208.25, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=208.25, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=247.9, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=287.55, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=287.55, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=327.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=366.85, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=366.85, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=406.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=446.15, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=446.15, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-171.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=49.65, default_y=-121.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.3, default_y=-131.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.95, default_y=-151.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.6, default_y=-116.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=208.25, default_y=-131.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=247.9, default_y=-171.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=287.55, default_y=-121.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=327.2, default_y=-141.01):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=366.85, default_y=-151.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=406.5, default_y=-116.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=446.15, default_y=-131.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='33', width=502.01):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=50.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=50.87, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=91.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=132.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=132.6, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=173.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=214.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=214.34, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=255.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=296.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=296.07, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=336.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=377.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=377.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=418.67, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=459.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=459.54, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-171.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.87, default_y=-116.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.73, default_y=-136.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=132.6, default_y=-151.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=173.47, default_y=-116.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=214.34, default_y=-136.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=255.2, default_y=-171.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=296.07, default_y=-121.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=336.94, default_y=-136.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=377.8, default_y=-146.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=418.67, default_y=-121.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=459.54, default_y=-136.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='34', width=485.09):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(86.07)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('258')
                Staff(1)
                Sound(tempo=258.0)
            with Note(default_x=111.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=141.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=141.77, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=13.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('238')
                Staff(1)
                Sound(tempo=238.0)
            with Note(default_x=172.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=202.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=202.88, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('218')
                Staff(1)
                Sound(tempo=218.0)
            with Note(default_x=233.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=263.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=263.99, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('208')
                Staff(1)
                Sound(tempo=208.0)
            with Note(default_x=294.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=325.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=325.11, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('198')
                Staff(1)
                Sound(tempo=198.0)
            with Note(default_x=355.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=386.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=386.22, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.92, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('188')
                Staff(1)
                Sound(tempo=188.0)
            with Note(default_x=416.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.92, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=447.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=447.33, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=111.21, default_y=-161.07):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=141.77, default_y=-111.07):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=172.33, default_y=-131.07):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.88, default_y=-141.07):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=233.44, default_y=-106.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=263.99, default_y=-131.07):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=294.55, default_y=-161.07):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=325.11, default_y=-116.07):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=355.66, default_y=-126.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=386.22, default_y=-141.07):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=416.78, default_y=-106.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=447.33, default_y=-126.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='35', width=532.06):
            with Attributes():
                with Key():
                    Fifths(-4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('268')
                Staff(1)
                Sound(tempo=268.0)
            with Note(default_x=93.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=130.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=130.19, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=166.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=202.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=202.96, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=239.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=275.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=275.74, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=312.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=348.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=348.52, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=384.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=421.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=421.29, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=457.68, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=494.07, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=494.07, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=93.8, default_y=-161.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=130.19, default_y=-116.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=166.58, default_y=-126.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.96, default_y=-131.07):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=239.35, default_y=-106.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=275.74, default_y=-126.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=312.13, default_y=-161.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=348.52, default_y=-116.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=384.91, default_y=-126.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=421.29, default_y=-131.07):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=457.68, default_y=-106.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=494.07, default_y=-126.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='36', width=531.76):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=51.97, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=51.97, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=93.94, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=138.91, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=138.91, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=180.88, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=231.36, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural-flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=231.36, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=45.9)
                Staff(1)
            with Note(default_x=273.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=315.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=315.3, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=357.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=399.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=399.24, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=441.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=483.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=483.19, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=10.0, default_y=-146.07):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=51.97, default_y=-101.07):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=93.94, default_y=-111.07):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=138.91, default_y=-116.07):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=180.88, default_y=-91.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=231.36, default_y=-111.07):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=273.33, default_y=-146.07):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=315.3, default_y=-101.07):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=357.27, default_y=-111.07):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=399.24, default_y=-116.07):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=441.21, default_y=-91.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=483.19, default_y=-111.07):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='37', width=591.15):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(95.7)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=123.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=160.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=160.35, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=196.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=233.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=233.44, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=269.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=306.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=306.52, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=370.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=406.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=406.85, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=443.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=479.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=479.93, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=516.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=553.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=553.01, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.1)
                Staff(2)
            with Note(default_x=123.81, default_y=-200.7):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=160.35, default_y=-165.7):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.89, default_y=-180.7):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=233.44, default_y=-190.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=269.98, default_y=-155.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=306.52, default_y=-180.7):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.1)
                Staff(2)
            with Note(default_x=370.31, default_y=-160.7):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=406.85, default_y=-115.7):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=443.39, default_y=-125.7):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=479.93, default_y=-135.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=516.47, default_y=-105.7):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=553.01, default_y=-125.7):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='38', width=484.17):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=49.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=49.32, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=88.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-2.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=128.74, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=128.74, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-2.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
            with Note(default_x=168.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=207.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=207.37, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=246.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=286.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=286.0, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=325.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=364.63, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=364.63, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=403.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=443.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=443.26, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.1)
                Staff(2)
            with Note(default_x=10.0, default_y=-155.7):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=49.32, default_y=-120.7):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=88.63, default_y=-130.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.74, default_y=-140.7):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.05, default_y=-105.7):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.37, default_y=-130.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.1)
                Staff(2)
            with Note(default_x=246.68, default_y=-155.7):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=286.0, default_y=-110.7):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=325.31, default_y=-125.7):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=364.63, default_y=-135.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=403.94, default_y=-100.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=443.26, default_y=-125.7):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='39', width=473.58):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=51.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=51.77, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=89.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=127.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=127.31, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=165.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=207.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=207.58, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=245.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=283.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=283.12, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=320.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=358.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=358.67, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=396.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=434.21, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=434.21, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.1)
                Staff(2)
            with Note(default_x=14.0, default_y=-155.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=51.77, default_y=-110.7):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.54, default_y=-130.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=127.31, default_y=-135.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=165.09, default_y=-100.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.58, default_y=-130.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.1)
                Staff(2)
            with Note(default_x=245.35, default_y=-165.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=283.12, default_y=-120.7):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=320.9, default_y=-130.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=358.67, default_y=-135.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=396.44, default_y=-100.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=434.21, default_y=-130.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='40', width=606.37):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(100.7)
            with Note(default_x=114.18, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=155.06, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=155.06, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=195.94, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=236.83, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=236.83, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=277.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=318.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=318.59, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=359.47, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=400.36, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=400.36, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=441.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=482.12, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=482.12, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=523.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=563.89, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=563.89, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=114.18, default_y=-155.7):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=155.06, default_y=-120.7):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.94, default_y=-135.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=236.83, default_y=-145.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=277.71, default_y=-110.7):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=318.59, default_y=-135.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=359.47, default_y=-175.7):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=400.36, default_y=-120.7):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=441.24, default_y=-130.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=482.12, default_y=-145.7):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=523.0, default_y=-110.7):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=563.89, default_y=-130.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='41', width=517.83):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=52.19, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=94.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=136.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=136.56, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=178.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=220.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=220.93, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=263.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=305.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=305.3, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=347.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=389.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=389.67, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=431.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=474.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=474.04, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-170.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=52.19, default_y=-120.7):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.37, default_y=-135.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=136.56, default_y=-145.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=178.74, default_y=-110.7):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=220.93, default_y=-135.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=263.11, default_y=-170.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=305.3, default_y=-120.7):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=347.49, default_y=-130.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=389.67, default_y=-145.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=431.86, default_y=-110.7):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=474.04, default_y=-130.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='42', width=424.71):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=44.43, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=78.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=113.28, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=113.28, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=147.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=182.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=182.13, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=216.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=250.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=250.98, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=285.41, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=319.83, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=319.83, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=354.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=388.68, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=388.68, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-170.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.43, default_y=-115.7):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=78.85, default_y=-125.7):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=113.28, default_y=-140.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=147.7, default_y=-105.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.13, default_y=-125.7):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=216.55, default_y=-170.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=250.98, default_y=-125.7):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=285.41, default_y=-135.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=319.83, default_y=-140.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=354.26, default_y=-125.7):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=388.68, default_y=-135.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='43', width=593.74):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(159.44)
                with StaffLayout(number=2):
                    StaffDistance(77.97)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=110.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=150.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.52, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=190.67, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=230.82, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=230.82, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=270.96, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=52.99)
                Staff(1)
            with Note(default_x=311.11, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=311.11, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=351.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=391.4, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=391.4, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=431.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=471.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=471.7, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=511.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=551.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=551.99, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=110.38, default_y=-132.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=110.38, default_y=-122.97):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=110.38, default_y=-97.97):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=230.46, default_y=-132.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=230.46, default_y=-117.97):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=217.87, default_y=-107.97):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=230.46, default_y=-102.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=471.7, default_y=-167.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='44', width=478.78):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=48.93, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=87.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=126.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=126.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=165.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=204.66, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=204.66, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=47.44)
                Staff(1)
            with Note(default_x=243.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=282.52, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=282.52, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=321.45, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=360.39, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=360.39, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=399.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=438.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=438.25, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-132.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-112.97):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=126.8, default_y=-132.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=126.8, default_y=-117.97):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=114.93, default_y=-107.97):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=126.8, default_y=-102.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=243.59, default_y=-167.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=360.39, default_y=-132.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=360.39, default_y=-117.97):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=348.52, default_y=-107.97):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=360.39, default_y=-102.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='45', width=476.39):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=48.61, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=87.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=125.82, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=125.82, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=164.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=203.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=203.04, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=243.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=281.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=281.75, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=320.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=358.97, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=358.97, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=397.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=436.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=436.18, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=10.0, default_y=-132.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=10.0, default_y=-122.97):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-112.97):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=48.61, default_y=-167.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
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
            with Note(default_x=203.04, default_y=-132.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=203.04, default_y=-112.97):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=243.14, default_y=-132.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=243.14, default_y=-102.97):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-2.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
            with Note(default_x=281.75, default_y=-167.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
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
            with Note(default_x=436.18, default_y=-132.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=436.18, default_y=-102.97):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-2.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='46', width=622.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(142.46)
                with StaffLayout(number=2):
                    StaffDistance(94.05)
            with Note(default_x=125.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=166.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=166.65, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=207.91, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=249.17, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=249.17, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=290.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=331.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=331.69, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=373.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=414.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=414.42, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=455.68, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=496.94, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=496.94, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=538.2, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=579.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=579.46, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=125.38, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=125.38, default_y=-124.05):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=166.65, default_y=-184.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
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
            with Note(default_x=331.69, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=331.69, default_y=-124.05):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=373.16, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural-flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=373.16, default_y=-114.05):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-2.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
            with Note(default_x=414.42, default_y=-184.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
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
            with Note(default_x=579.46, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=579.46, default_y=-114.05):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-2.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='47', width=417.39):
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=47.3, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=80.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=114.3, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=114.3, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=147.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=181.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=181.3, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=214.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=248.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=248.29, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=281.79, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=31.32)
                Staff(1)
            with Note(default_x=315.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=315.29, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=348.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=382.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=382.29, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=13.8, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=13.8, default_y=-119.05):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=47.3, default_y=-184.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
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
            with Note(default_x=181.3, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=181.3, default_y=-119.05):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=214.79, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=214.79, default_y=-109.05):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=248.29, default_y=-184.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
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
            with Note(default_x=382.29, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=382.29, default_y=-109.05):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='48', width=509.19):
            with Note(default_x=14.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=55.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=55.13, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=96.27, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=137.4, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.4, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=178.53, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=219.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=219.66, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=260.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=301.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=301.93, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=343.06, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=34.5, relative_x=-18.77)
                Staff(1)
            with Note(default_x=384.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=384.19, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1, relative_x=5.75)
                Staff(1)
            with Note(default_x=425.33, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=466.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=466.46, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=14.0, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=14.0, default_y=-114.05):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=55.13, default_y=-184.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
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
            with Note(default_x=219.66, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=219.66, default_y=-114.05):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=260.8, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=260.8, default_y=-104.05):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=301.93, default_y=-184.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
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
            with Note(default_x=466.46, default_y=-149.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=466.46, default_y=-104.05):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='49', width=554.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(154.26)
                with StaffLayout(number=2):
                    StaffDistance(87.44)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.01, relative_y=-26.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=110.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=145.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=145.61, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=180.84, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=60.5)
                Staff(1)
            with Note(default_x=235.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=235.63, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=270.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=306.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=306.1, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=341.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=376.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=376.56, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=411.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=447.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=447.03, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=482.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=517.49, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=517.49, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=110.38, default_y=-142.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=110.38, default_y=-122.44):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=110.38, default_y=-112.44):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=110.38, default_y=-97.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=7.0, relative_y=-22.0):
                        Fz()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=235.27, default_y=-147.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=235.27, default_y=-137.44):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=235.27, default_y=-122.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=154.47)
                Staff(2)
            with Note(default_x=447.03, default_y=-152.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=447.03, default_y=-137.44):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=447.03, default_y=-127.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='50', width=505.18):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('diminuendo e leggierissimo', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=50.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=50.82, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=91.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=136.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=136.18, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=177.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=217.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=217.83, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=258.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=299.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=299.47, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=340.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=381.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=381.11, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=421.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=462.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=462.76, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-147.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=1)
            with Note(default_x=10.0, default_y=-137.44):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=10.0, default_y=-122.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=136.18, default_y=-152.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=136.18, default_y=-137.44):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=136.18, default_y=-127.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=258.65, default_y=-147.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=258.65, default_y=-137.44):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=258.65, default_y=-122.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=381.11, default_y=-137.44):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=381.11, default_y=-122.44):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Forward():
                Duration(9.0)
            with Note(default_x=381.11, default_y=-147.44):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='51', width=489.4):
            with Note(default_x=10.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=50.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=50.15, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=89.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=129.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=129.72, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=169.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=209.29, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=249.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=288.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=288.87, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=328.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=368.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=368.44, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=408.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=448.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=448.02, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-132.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=10.0, default_y=-122.44):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=248.72, default_y=-137.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=248.72, default_y=-127.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-147.44):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=129.36, default_y=-152.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=368.44, default_y=-157.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='52', width=535.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(156.13)
                with StaffLayout(number=2):
                    StaffDistance(72.55)
            with Note(default_x=131.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=164.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.88, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=198.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=231.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=231.89, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=265.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=298.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=298.91, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=332.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=365.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=365.92, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=399.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=432.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=432.93, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=466.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=499.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=499.94, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=131.01, default_y=-122.55):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=131.01, default_y=-112.55):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=332.05, default_y=-127.55):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=332.05, default_y=-117.55):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=131.37, default_y=-142.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=231.53, default_y=-142.55):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=432.93, default_y=-147.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='53', width=462.11):
            with Note(default_x=34.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=69.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.04, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=103.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=140.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=140.9, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=175.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=209.7, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=244.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=278.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=278.5, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=312.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=347.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=347.29, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=381.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=416.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=416.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=34.28, default_y=-127.55):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=34.28, default_y=-117.55):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-2.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('flat-flat')
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
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(12.0)
            with Note(default_x=34.64, default_y=-147.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=140.9, default_y=-147.55):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(6.0)
        with Measure(number='54', width=551.75):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dolciss.', default_y=-46.73, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=34.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('258')
                Staff(1)
                Sound(tempo=258.0)
            with Note(default_x=16.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('rallent.', relative_x=-25.0, relative_y=20.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=60.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.65, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=46.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('238')
                Staff(1)
                Sound(tempo=238.0)
            with Note(default_x=105.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1, relative_x=-6.13)
                Staff(1)
            with Note(default_x=150.07, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=150.07, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=41.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('218')
                Staff(1)
                Sound(tempo=218.0)
            with Note(default_x=194.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=238.98, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=238.98, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=36.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('198')
                Staff(1)
                Sound(tempo=198.0)
            with Note(default_x=283.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-2.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=327.88, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=327.88, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-2.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=13.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('178')
                Staff(1)
                Sound(tempo=178.0)
            with Note(default_x=372.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=416.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-2.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=416.79, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('158')
                Staff(1)
                Sound(tempo=158.0)
            with Note(default_x=461.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('72')
                Staff(1)
                Sound(tempo=72.0)
            with Note(default_x=505.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=505.69, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=16.2, default_y=-157.55):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=105.11, default_y=-137.55):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=150.07, default_y=-127.55):
                with Pitch():
                    Step('E')
                    Alter(-2.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=194.53, default_y=-112.55):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=238.98, default_y=-92.55):
                with Pitch():
                    Step('E')
                    Alter(-2.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=283.43, default_y=-77.55):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
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
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='55', width=665.3):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(151.64)
                with StaffLayout(number=2):
                    StaffDistance(96.07)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', default_y=20.33, relative_y=20.0, font_weight='bold', font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=268.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=110.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=156.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=156.49, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=202.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=248.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=248.71, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=294.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=340.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=340.93, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=387.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=433.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=433.15, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=479.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=525.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=525.37, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=571.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=77.78)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-57.84)
                Staff(1)
            with Note(default_x=617.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=617.59, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=110.38, default_y=-171.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=156.49, default_y=-126.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.6, default_y=-136.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=248.71, default_y=-151.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=294.82, default_y=-116.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=340.93, default_y=-136.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=387.04, default_y=-171.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=433.15, default_y=-126.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=479.26, default_y=-136.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=525.37, default_y=-151.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=571.48, default_y=-116.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=617.59, default_y=-136.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='56', width=444.9):
            with Note(default_x=16.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=51.79, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.79, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=87.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-59.06)
                Staff(1)
            with Note(default_x=122.98, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=122.98, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=158.57, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=194.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=194.16, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=229.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=265.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=265.34, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=300.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=336.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=336.53, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=372.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=407.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=407.71, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=16.2, default_y=-171.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=51.79, default_y=-121.07):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=87.38, default_y=-141.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=122.98, default_y=-151.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.57, default_y=-116.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=194.16, default_y=-141.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=229.75, default_y=-171.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=265.34, default_y=-126.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=300.93, default_y=-136.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=336.53, default_y=-151.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=372.12, default_y=-116.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=407.71, default_y=-136.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='57', width=438.7):
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=45.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=45.59, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=81.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=116.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=116.78, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=152.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=187.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=187.96, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=223.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=259.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=259.14, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=294.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=330.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=330.33, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=365.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=401.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=401.51, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-171.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=45.59, default_y=-121.07):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.18, default_y=-141.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=116.78, default_y=-151.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=152.37, default_y=-116.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=187.96, default_y=-141.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=223.55, default_y=-171.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=259.14, default_y=-126.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=294.73, default_y=-136.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=330.33, default_y=-151.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=365.92, default_y=-116.07):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=401.51, default_y=-136.07):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='58', width=455.64):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(143.06)
                with StaffLayout(number=2):
                    StaffDistance(85.76)
            with Note(default_x=110.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=140.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=140.84, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=168.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=196.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=196.77, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=224.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=252.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=252.7, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=281.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=314.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=314.23, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=342.19, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=370.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=370.15, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=398.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=426.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=426.08, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=110.38, default_y=-155.76):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.84, default_y=-110.76):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.81, default_y=-120.76):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.77, default_y=-125.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=224.73, default_y=-110.76):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=252.7, default_y=-120.76):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=281.56, default_y=-175.76):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=314.23, default_y=-110.76):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=342.19, default_y=-120.76):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=370.15, default_y=-140.76):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=398.12, default_y=-110.76):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=426.08, default_y=-120.76):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='59', width=396.58):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=40.76, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=71.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=102.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=102.28, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=133.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=167.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=167.93, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=198.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=229.45, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=229.45, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=260.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=302.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=302.71, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=333.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=364.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=364.23, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=10.0, default_y=-160.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=40.76, default_y=-115.76):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=71.52, default_y=-125.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=102.28, default_y=-140.76):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.04, default_y=-105.76):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=167.93, default_y=-125.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=198.69, default_y=-160.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=229.45, default_y=-115.76):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=260.21, default_y=-125.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=302.71, default_y=-140.76):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=333.47, default_y=-105.76):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=364.23, default_y=-125.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='60', width=335.59):
            with Note(default_x=16.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=42.68, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=42.68, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=69.17, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.65, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=95.65, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=122.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=148.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=148.61, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=175.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=201.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=201.58, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=228.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=254.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=254.54, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=281.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=307.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=307.51, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=16.2, default_y=-160.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.68, default_y=-110.76):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=69.17, default_y=-130.76):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.65, default_y=-140.76):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=122.13, default_y=-105.76):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.61, default_y=-130.76):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=175.1, default_y=-160.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=201.58, default_y=-115.76):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=228.06, default_y=-125.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=254.54, default_y=-140.76):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=281.03, default_y=-105.76):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=307.51, default_y=-125.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='61', width=361.09):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=39.0, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=68.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=97.01, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=126.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=155.01, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=155.01, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=184.01, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=214.48, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=214.48, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=243.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=272.48, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=272.48, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=301.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=330.49, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=330.49, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=10.0, default_y=-145.76):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.0, default_y=-100.76):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.0, default_y=-110.76):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.01, default_y=-125.76):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=126.01, default_y=-100.76):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=155.01, default_y=-110.76):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.02)
                Staff(2)
            with Note(default_x=184.01, default_y=-150.76):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=214.48, default_y=-105.76):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.48, default_y=-115.76):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=272.48, default_y=-120.76):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=301.48, default_y=-95.76):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=330.49, default_y=-115.76):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='62', width=435.84):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(89.02)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=110.38, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=136.89, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=136.89, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=163.4, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=189.92, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=189.92, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=218.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=248.65, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=248.65, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=275.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=301.68, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=301.68, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=328.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=354.7, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=354.7, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=381.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=407.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=407.73, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=110.38, default_y=-139.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=136.89, default_y=-104.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.4, default_y=-119.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=189.92, default_y=-129.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=218.18, default_y=-94.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=248.65, default_y=-119.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=275.16, default_y=-149.02):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=301.68, default_y=-104.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=328.19, default_y=-124.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=354.7, default_y=-129.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=381.22, default_y=-104.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=407.73, default_y=-124.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='63', width=382.06):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.5, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=40.5, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=71.17, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.83, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=103.83, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=134.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=164.82, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=164.82, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=195.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=225.82, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=225.82, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=256.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=286.81, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=286.81, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=317.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=349.97, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=349.97, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=10.0, default_y=-144.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=40.5, default_y=-109.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=71.17, default_y=-119.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=103.83, default_y=-129.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=134.33, default_y=-94.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=164.82, default_y=-119.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=195.32, default_y=-144.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=225.82, default_y=-99.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=256.31, default_y=-114.02):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=286.81, default_y=-124.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=317.3, default_y=-99.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=349.97, default_y=-114.02):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='64', width=356.52):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-76.3)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=45.42)
                Staff(1)
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=38.34, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=66.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=95.02, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=123.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-41.3, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=77.78)
            with Note(default_x=151.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=151.69, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=180.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=212.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=212.7, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=241.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=269.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=269.9, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=298.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=77.78)
            with Note(default_x=326.58, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=326.58, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=10.0, default_y=-139.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.34, default_y=-104.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=66.68, default_y=-119.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.02, default_y=-129.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=123.36, default_y=-94.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.69, default_y=-119.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=180.03, default_y=-149.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=212.7, default_y=-104.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=241.04, default_y=-124.02):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=269.9, default_y=-129.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=298.24, default_y=-94.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=326.58, default_y=-124.02):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='65', width=374.48):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.76, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=38.76, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=69.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=102.1, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=102.1, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=130.85, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.61, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=159.61, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=188.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=223.27, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=223.27, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=253.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=286.6, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=286.6, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=315.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=344.12, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=344.12, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=10.0, default_y=-144.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.76, default_y=-94.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=69.43, default_y=-109.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=102.1, default_y=-119.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=130.85, default_y=-94.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=159.61, default_y=-109.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=188.37, default_y=-144.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=223.27, default_y=-94.02):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=253.94, default_y=-109.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=286.6, default_y=-119.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=315.36, default_y=-94.02):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=344.12, default_y=-109.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='66', width=553.06):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(85.62)
            with Note(default_x=110.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=147.14, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=147.14, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=183.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=220.65, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=220.65, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=257.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=294.16, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=294.16, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=330.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=367.68, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=367.68, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=404.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=429.33, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=441.19, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=477.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=514.71, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=514.71, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=110.38, default_y=-140.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=147.14, default_y=-95.62):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.89, default_y=-105.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=220.65, default_y=-110.62):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=257.41, default_y=-85.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=294.16, default_y=-105.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=330.92, default_y=-140.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=367.68, default_y=-95.62):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=404.44, default_y=-105.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=441.19, default_y=-110.62):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=477.95, default_y=-95.62):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=514.71, default_y=-105.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='67', width=510.37):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=51.56, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=51.56, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=93.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=134.69, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=134.69, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-76.32)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-76.32)
                Staff(1)
            with Note(default_x=176.26, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=217.82, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=217.82, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=259.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=300.95, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=300.95, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=342.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=384.08, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=384.08, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=425.64, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=467.21, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=467.21, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=10.0, default_y=-140.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=51.56, default_y=-90.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=93.13, default_y=-105.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=134.69, default_y=-115.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=176.26, default_y=-90.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=217.82, default_y=-105.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=259.39, default_y=-140.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=300.95, default_y=-90.62):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=342.51, default_y=-105.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=384.08, default_y=-115.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=425.64, default_y=-90.62):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=467.21, default_y=-105.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='68', width=485.47):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=113.33)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=37.92, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('258')
                Staff(1)
                Sound(tempo=258.0)
            with Note(default_x=14.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('poco rit.', default_y=-40.0, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=53.16, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=53.16, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=33.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('238')
                Staff(1)
                Sound(tempo=238.0)
            with Note(default_x=92.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=131.47, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.47, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=38.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('218')
                Staff(1)
                Sound(tempo=218.0)
            with Note(default_x=170.62, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=209.78, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=209.78, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=31.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('198')
                Staff(1)
                Sound(tempo=198.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=248.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=35.42)
                Staff(1)
            with Note(default_x=288.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=288.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=23.72, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('178')
                Staff(1)
                Sound(tempo=178.0)
            with Note(default_x=327.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=366.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=366.4, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=23.72, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('158')
                Staff(1)
                Sound(tempo=158.0)
            with Note(default_x=405.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=23.72, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('88')
                Staff(1)
                Sound(tempo=88.0)
            with Note(default_x=444.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=444.72, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=14.0, default_y=-140.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=53.16, default_y=-90.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.31, default_y=-110.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=131.47, default_y=-120.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=170.62, default_y=-90.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=209.78, default_y=-110.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=248.94, default_y=-140.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=288.09, default_y=-95.62):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=327.25, default_y=-105.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=366.4, default_y=-110.62):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=405.56, default_y=-95.62):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=444.72, default_y=-105.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='69', width=555.63):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(75.62)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', relative_y=58.44, font_weight='bold', font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=268.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=110.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=146.85, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=183.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=219.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=219.78, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=256.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=292.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=292.72, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=329.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=365.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=365.66, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=402.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=444.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=444.62, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=481.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=517.56, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=517.56, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=110.38, default_y=-150.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=146.85, default_y=-105.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.31, default_y=-115.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.78, default_y=-130.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=256.25, default_y=-95.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=292.72, default_y=-115.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=329.19, default_y=-150.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=365.66, default_y=-105.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=402.13, default_y=-115.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=444.62, default_y=-130.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=481.09, default_y=-95.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=517.56, default_y=-115.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='70', width=335.23):
            with Note(default_x=16.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=42.65, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=42.65, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=69.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=95.56, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.56, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=122.01, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.46, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=148.46, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Words('sempre dim. e legatissimo', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=174.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=201.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=201.37, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=227.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=254.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=254.27, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=280.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=307.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=307.17, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=16.2, default_y=-150.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.65, default_y=-100.62):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=69.1, default_y=-120.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.56, default_y=-130.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=122.01, default_y=-95.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.46, default_y=-120.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=174.91, default_y=-150.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=201.37, default_y=-105.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=227.82, default_y=-115.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=254.27, default_y=-130.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=280.72, default_y=-95.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=307.17, default_y=-115.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='71', width=329.03):
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=36.45, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=62.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=89.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=89.36, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=115.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=142.26, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=168.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=195.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=195.17, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=221.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=248.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=248.07, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=274.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=300.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=300.97, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-150.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.45, default_y=-100.62):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=62.9, default_y=-120.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.36, default_y=-130.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=115.81, default_y=-95.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=142.26, default_y=-120.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=168.71, default_y=-150.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=195.17, default_y=-105.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=221.62, default_y=-115.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=248.07, default_y=-130.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.52, default_y=-95.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=300.97, default_y=-115.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='72', width=329.03):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.45, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=36.45, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=62.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=89.36, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=89.36, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=115.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.26, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=142.26, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=168.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=195.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=195.17, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=221.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=248.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=248.07, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=274.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=300.97, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=300.97, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-150.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.45, default_y=-100.62):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=62.9, default_y=-120.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.36, default_y=-130.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=115.81, default_y=-95.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=142.26, default_y=-120.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=168.71, default_y=-150.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=195.17, default_y=-105.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=221.62, default_y=-115.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=248.07, default_y=-130.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.52, default_y=-95.62):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=300.97, default_y=-115.62):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='73', width=479.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(91.97)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('258')
                Staff(1)
                Sound(tempo=258.0)
            with Note(default_x=110.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=140.97, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=140.97, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=171.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=13.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('248')
                Staff(1)
                Sound(tempo=248.0)
            with Note(default_x=202.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=202.17, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=232.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=263.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=263.36, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('238')
                Staff(1)
                Sound(tempo=238.0)
            with Note(default_x=293.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=324.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=324.55, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=355.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('228')
                Staff(1)
                Sound(tempo=228.0)
            with Note(default_x=385.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=385.74, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=416.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=446.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=446.93, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=110.38, default_y=-166.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.97, default_y=-116.97):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=171.57, default_y=-136.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.17, default_y=-146.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=232.76, default_y=-111.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=263.36, default_y=-136.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.51)
                Staff(2)
            with Note(default_x=293.95, default_y=-166.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=324.55, default_y=-121.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=355.14, default_y=-131.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=385.74, default_y=-146.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=416.33, default_y=-111.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=446.93, default_y=-131.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='74', width=342.99):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('218')
                Staff(1)
                Sound(tempo=218.0)
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Direction(placement='below'):
                with DirectionType():
                    Words('smorz.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=37.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=37.62, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=65.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('208')
                Staff(1)
                Sound(tempo=208.0)
            with Note(default_x=92.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=92.85, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=120.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=148.08, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('198')
                Staff(1)
                Sound(tempo=198.0)
            with Note(default_x=175.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=203.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=203.31, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=230.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('188')
                Staff(1)
                Sound(tempo=188.0)
            with Note(default_x=258.54, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=258.54, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=286.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=313.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=313.77, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-166.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=37.62, default_y=-121.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=65.23, default_y=-131.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.85, default_y=-146.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=120.46, default_y=-111.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.08, default_y=-131.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=175.69, default_y=-166.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=203.31, default_y=-121.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=230.92, default_y=-131.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=258.54, default_y=-146.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=286.16, default_y=-111.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=313.77, default_y=-131.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='75', width=312.45):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=10.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=34.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=34.26, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=58.15, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=82.05, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=82.05, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=105.94, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=129.84, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=153.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=177.63, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=177.63, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=201.53, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=230.39, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=230.39, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=230.39, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=254.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=286.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=286.95, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=286.95, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.11)
                Staff(2)
            with Note(default_x=10.0, default_y=-166.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.18)
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=230.39, default_y=-186.97):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=230.39, default_y=-151.97):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=60.07)
                Staff(2)
        with Measure(number='76', width=321.13):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=28.6, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('178')
                Staff(1)
                Sound(tempo=178.0)
            with Note(default_x=17.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=42.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=42.32, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=42.32, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=67.52, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=38.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('168')
                Staff(1)
                Sound(tempo=168.0)
            with Note(default_x=92.72, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=92.72, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=92.72, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=117.92, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('riten.', default_y=-63.9, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=143.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=143.12, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=143.12, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=21.4, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('148')
                Staff(1)
                Sound(tempo=148.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('ten.', relative_y=20.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=168.32, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=21.4, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('128')
                Staff(1)
                Sound(tempo=128.0)
            with Note(default_x=193.53, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=193.53, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('108')
                Staff(1)
                Sound(tempo=108.0)
            with Note(default_x=218.73, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=12.26, relative_y=66.59):
                        BeatUnit('quarter')
                        PerMinute('88')
                Staff(1)
                Sound(tempo=88.0)
            with Note(default_x=243.93, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=243.93, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Staff(1)
                Sound(tempo=68.0)
            with Note(default_x=269.13, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=269.13, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=2.45, relative_y=44.52):
                        BeatUnit('quarter')
                        PerMinute('48')
                Staff(1)
                Sound(tempo=48.0)
            with Note(default_x=294.33, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=294.33, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=167.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.11)
                Staff(2)
            with Note(default_x=13.8, default_y=-201.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-166.97):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='77', width=93.21):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=12.26, relative_y=11.42):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=21.68, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
            with Note(default_x=21.68, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
            with Note(default_x=21.68, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.68, default_y=-201.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=21.68, default_y=-166.97):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')